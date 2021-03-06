from __future__ import print_function
import re,itertools
import copy
import sys
import os
import shutil
sys.path.append('../layout/')
sys.path.append('./layout/')
sys.path.append('../src/')
sys.path.append('../layout/navbar/')
sys.path.append('../layout/footer/')
sys.path.append('./layout/navbar/')
sys.path.append('./layout/footer/')
import ply.yacc as yacc
from HTML_slideshow import *
from HTML_navbar import *
from HTML_footer import *
from makeCSS import makeCSS
from lexer import tokens,styles,keywords
from pyparsing import *
def eprint(*args, **kwargs):
	print (*args, file=sys.stderr, **kwargs)

LineNumber=1
#eprint(str(CSSCount['hover-button']))
CSSCount = {
	'navbar':1,
	'footer':1,
	'button':1,
	'hover-button':1,
	'click-button':1,
	'piechart':1,
	'card':1,
	'fade':1,
	'image':1,
	'link':1,
	'hoverdropdown':1,
	'list':1,
	'flip':1,
	'shake':1,
	'table':1,
	'slideshow':1,
	'parallax':1,
	'accordion':1,
	'timeline':1,
	'checkbox':1,
	'alert':1,
	'grid':1,
	'wallpaper':1,
	'skillbar':1,
	'tooltip':1,
	'chatbox':1,
	'textfield':1,
	'passwordfield':1,
	'select':1,
	'submit':1,
	'block':1,
	'aparallax':1,
	'terminal':1,
	'iconbar':1,
	'wallpaper2':1,
	'enlarge':1
}
#---------------------------------------------------------------------------------------
# This function makes a dictionary out of a string as shown below
# string = 'home:url , about:url , contact:url'
# It first splits the string with commas and then within each part takes the first colon as the separating element
def dictionaryMaker(s):
	final_dict = {};
	for temp in s.split(','):
		# temp is 'home:url'
		i = temp.find(':')
		final_dict[temp[:i].strip()] = temp[i+1:].strip()
	return final_dict

# This function makes a list of tuples out of a string as shown below
# string = 'home:url , about:url , contact:url'
# It differs from the above function that this maintains the order of element inside
def listoftupleMaker(s):
	final_list = []
	for temp in s.split(','):
		# temp is 'home:url'
		i = temp.find(':')
		final_list.append((temp[:i].strip(),temp[i+1:].strip()))
	return final_list
#---------------------------------------------------------------------------------------


def isContained(s):
	keywords = {'id':False , 'href':False , 'class':False , 'width':True , 'height':True , 'background-color':True , 'font-size':True , 'float':True}
	return keywords[s]

def attributeString(d):
	keywords = list(d.keys())
	standalone_str = ""
	contained_str = ""
	for keyword in keywords:
		if(isContained(keyword)):
			contained_str = contained_str + ('%s:%s;')%(keyword,d[keyword])
		else:
			standalone_str = standalone_str + (' %s="%s"')%(keyword,d[keyword])
	if contained_str == "":
		return (standalone_str)
	elif standalone_str == "":
		return  (('style="%s"')%contained_str)
	else:
		return (standalone_str) + (('style="%s"')%contained_str)

def ContainerElement(d,newline):
	if not(isinstance(d,dict)):
		return d
	else:
		container_name = list(d.keys())
		container_name.remove('content');
		result = ""
		if (newline):
			result = '\n'.join((('<%s%s>'%(container_name[0] , attributeString(d[container_name[0]]))) , d['content'] ,('</%s>'%container_name[0])))
		else:
			result = ''.join((('<%s%s>'%(container_name[0] , attributeString(d[container_name[0]]))) , d['content'] ,('</%s>'%container_name[0])))
		return result

# POWERFUL FUNCTION
def recursiveBuild(dictionary):
	container_name = list(dictionary.keys())
	if not(isinstance(dictionary['content'],dict)):
		return ContainerElement(dictionary, False)
	else:
		inner = recursiveBuild(dictionary['content'])
		dictionary['content'] = inner
		return ContainerElement(dictionary,True);

DirectChangeStyles={"bold":"b","h2":"h2","h1":"h1","h3":"h3","h4":"h4","h5":"h5","h6":"h6","italic":"i","underline":"u" ,"center":"center","code":'code', "sup":'sup' , "sub":'sub' , "kbd":'kbd' , 'quote':'blockquote'}
IndirectChangeStyles={'latex':'lang:"latex"' ,'r':'text-align:right','l':'text-align:left','c':'text-align:center', 'danger':'background-color: #ffdddd;border-left: 6px solid #f44336; margin-bottom:15px;padding:10px 12px',
'info':'background-color: #e7f3fe;border-left: 6px solid #2196F3;margin-bottom:15px;padding:10px 12px','success':'background-color: #d1ffa0;border-left: 6px solid #4CAF50;margin-bottom:15px;padding:10px 12px' , 'warning':'background-color: #ffffcc;border-left: 6px solid #ffeb3b;margin-bottom:15px;padding:10px 12px'}

#This function is called from styleMaker and takes strings(style and content) as arguments
#style contains formatting styles to be implemented on content
#Returns a dictionary for generating HTML 
def taggedMaker(style,content):
	if(not style):
		return content
	else:
		style=style.split(',')
		style=[IndirectChangeStyles[x] if x in IndirectChangeStyles else x for x in style]
		ltagged=[]
		htagged=[]
		for x in style:
			if(':' in x):
				htagged.append(x)
			else:
				ltagged.append(x)
		if(ltagged and htagged):
			htagged=';'.join(htagged)+';'
			ltaggedStart=''.join(['<'+DirectChangeStyles[x]+'>' for x in ltagged])
			ltaggedEnd=''.join(['</'+DirectChangeStyles[x]+'>' for x in ltagged[::-1]])
			if('align' in htagged or 'text-align' in htagged):
				return "<div style=\""+htagged+"\">"+ltaggedStart+content+ltaggedEnd+"</div>\n"
			else:
				return "<span style=\""+htagged+"\">"+ltaggedStart+content+ltaggedEnd+"</span>\n"
		elif(ltagged):
			ltaggedStart=''.join(['<'+str(DirectChangeStyles[x])+'>' for x in ltagged])
			ltaggedEnd=''.join(['</'+str(DirectChangeStyles[x])+'>' for x in ltagged[::-1]])
			return ltaggedStart+content+ltaggedEnd
		elif(htagged):
			htagged=';'.join(htagged)+';'
			if('align' in htagged or 'text-align' in htagged):
				return "<div style=\""+htagged+"\">"+content+"</div>\n"
			else:
				return "<span style=\""+htagged+"\">"+content+"</span>\n"

TwoNonCSS={'class':'class', 'data-ride':'data-ride', 'data-slide':'data-slide','id':'id','text':'alt','download':'download','border':'border','caption':'caption','cursor':'cursor','margin':'margin','padding':'padding','float':'float','type':'type',
'width':'width','height':'height','scale':'scale','align':'align','data-target':'data-target','data-slide-to':'data-slide-to','opacity':'opacity','cursor':'cursor','symbol':'type','background-color':'background-color','font-color':'font-color','color':'color','text-color':'text-color','font-size':'font-size'}
OneNonCSS={'rounded':{'class':'img-rounded'},'circle':{'class':'img-circle'},'download':{'download':'Untitled_File'},
'indented':{'list-style-position':'inside'},'striped':{'class':'striped'},'bordered':{'class':'bordered'},'condensed':{'class':'condensed'},
'hover':{'class':'hover'},'round':{'rounded':'8px'},'oval':{'rounded':'50%'},'shadow':{'shadow':'0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)'},
'hover-shadow':{'hover-shadow':'0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19)'},'disabled':{'opacity':'0.6','cursor':'not-allowed'}}

#This function is called from styleMaker and takes strings(style and content) as arguments
#style contains formatting styles such as label to be implemented on the piechart
#content contains data or file(present in pages folder) from which data is taken as input
#Returns a dictionary for generating HTML 
#Used for making piechart
def piechartMaker(style,content):
	style=style.split(',')
	r1 = re.compile("\s*label.*")
	styleLabel = list(filter(r1.match, style))[0]
	r1 = re.compile("\s*type.*")
	styleType = list(filter(r1.match, style))[0]
	r2=re.compile("(?!(\s*label|\s*type)).*")
	styleStyle=list(filter(r2.match, style))
	if ',' in content:
		tempFile=open("./tmp/"+styleLabel.split(':')[1].strip()+".csv",'w')
		tempFile.write(content.replace(',','\n').replace(':',','))
		tempFile.close()
	else:
		shutil.copy("./pages/"+content.strip(),"./tmp/"+styleLabel.split(':')[1].strip()+".csv")
	file=open("./layout/GNUPlot/piechart_"+styleType.split(':')[1].strip()+".plot")
	newFile=open("./tmp/"+styleLabel.split(':')[1].strip()+".plot",'w')
	line=file.readline()
	templine=''
	while(line):
	    if("XXXXX" in line):
	        templine=templine+line.replace("XXXXX","./tmp/"+styleLabel.split(':')[1].strip()+".csv")
	    elif("YYYYY" in line):
	        templine=templine+line.replace("YYYYY","./site/img/"+styleLabel.split(':')[1].strip()+".png")
	    else:
	        templine=templine+line
	    line=file.readline()
	newFile.write(templine)
	piechartDict={'img':{'src':'img/'+styleLabel.split(':')[1].strip()+'.png'},'content':{}}
	if(styleStyle):
		tempDict={x[:x.find(':')].strip():x[x.find(':')+1:].strip() for x in styleStyle}
		piechartDict['img'].update(tempDict)
		return piechartDict
	else:
		return piechartDict

#This function is called from styleMaker and takes strings(style and content) as arguments
#style contains formatting styles to be implemented on button and also some special types such as hover-dropdown,click-dropdown
#content contains name of button and its dropdown elements with links
#Returns a dictionary for generating HTML 
#Used for making buttons
def buttonMaker(style,content):
	sendDict={'class':'#button'+str(CSSCount['button'])}
	tempDict={y[:y.find(':')].strip():y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1)]}
	for x in [OneNonCSS[x.strip()] for x in style.split(',') if x.find(':')==-1 and x.strip() in OneNonCSS.keys()]:
		for (key,value) in x.items():
			if key in tempDict.keys():
				tempDict[key]=tempDict[key]+' '+value
			else:
				tempDict[key]=value
	sendDict.update(tempDict)
	if('hover-dropdown' in style):
		buttonDict={'div':{'id':'hover-button'+str(CSSCount['hover-button'])},'content':{1:{'button':{'class':'dropbtn'},'content':{}},2:{'div':{'class':'dropdown-content'},'content':{}}}}
		sendDict['class']='#hover-button'+str(CSSCount['hover-button'])
		sendDict={'hover-button':sendDict}
		i=1
		tmpDict={}
		for x in content.split(','):
			if x.find(':')==-1:
				buttonDict['content'][1]['content']=x.strip();
			else:
				tmpDict.update({i:{'a':{'href':x[x.find(':')+1:].strip()},'content':x[:x.find(':')].strip()}})
				i=i+1
		buttonDict['content'][2]['content']=tmpDict
		#eprint("EH")
		CSSCount['hover-button']=CSSCount['hover-button']+1
	elif('click-dropdown' in style):
		buttonDict={'div':{'class':'clickdropdown'},'content':{1:{'button':{'class':'clickdropbtn','onclick':'myFunction()'},'content':{}},2:{'div':{'class':'clickdropdown-content','id':'myDropdown'},'content':''}}}
		sendDict={'click-button':sendDict}
		i=1
		tmpDict={}
		for x in content.split(','):
			if x.find(':')==-1:
				buttonDict['content'][1]['content']=x.strip();
			else:
				tmpDict.update({i:{'a':{'href':x[x.find(':')+1:].strip()},'content':x[:x.find(':')].strip()}})
				i=i+1
		buttonDict['content'][2]['content']=tmpDict
		makeJS({'click-dropdown':{}})
	else:
		sendDict={'button':sendDict}
		buttonDict={'button':{'id':'button'+str(CSSCount['button'])},'content':content.strip()}
		CSSCount['button']=CSSCount['button']+1
	makeCSS(sendDict)
	return buttonDict
#This function is called from styleMaker and takes strings(style and content) as arguments
#style contains formatting styles to be implemented on card
#content contains caption:image 
#Returns a dictionary for generating HTML 
#Used for making cards
def cardMaker(style,content):
	cardDict={'div':{'id':'card'+str(CSSCount['card'])},'content':{
		1:{'div':{'class':'polaroid'},'content':{
			1:{'img':{},'content':''},
			2:{'div':{'class':'container'},'content':{
				1:{'p':{},'content':''}}}}}}}
	sendDict={'class':'#card'+str(CSSCount['card'])}
	if content.find(':') != -1:
		cardDict['content'][1]['content'][2]['content'][1]['content']=content.split(':')[0].strip()
		cardDict['content'][1]['content'][1]['img']['src']= 'img/' + content.split(':')[1].strip()
	else:
		del cardDict['content'][1]['content'][2]
		cardDict['content'][1]['content'][1]['img']['src']= 'img/' + content.strip()	
	styleDict={y[:y.find(':')].strip():y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1)]}
	for x in ['color','font-color','font-size','padding-top','padding-left']:
		if x in styleDict.keys():
			sendDict[x]=styleDict[x]
			del styleDict[x]
	cardDict['content'][1]['content'][1]['img'].update(styleDict)
	sendDict={'card':sendDict}
	makeCSS(sendDict)
	CSSCount['card']=CSSCount['card']+1
	eprint(cardDict)
	return cardDict
#This function is called from styleMaker and takes strings(style and content) as arguments
#style contains formatting styles to be implemented on card
#content contains caption:image 
#Returns a dictionary for generating HTML 
#Used for making fade(when )
def fadeMaker(style,content):
	fadeDict={'div':{'id':'fade'+str(CSSCount['fade'])},'content':{ 1:{
				'div':{'class':'container'},'content':{
					1:{'img':{'class':'image'},'content':''},
					2:{'div':{'class':'overlay'},'content':{
						1:{'div':{'class':'text'},'content':''}}}}}}}
	fadeDict['content'][1]['content'][2]['content'][1]['content'] = content.split(':')[0].strip()
	fadeDict['content'][1]['content'][1]['img']['src']= 'img/' + content.split(':')[1].strip()
	sendDict={'class':'#fade'+str(CSSCount['fade'])}
	if(style.split(',')[0].strip()=='top' or style.split(',')[0].strip()=='bottom' or style.split(',')[0].strip()=='left' or style.split(',')[0].strip()=='right'):
		sendDict['type']=style.split(',')[0].strip()
	else:
		sendDict['type']=None
	styleDict={y[:y.find(':')].strip():y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1)]}
	for x in ['color','font-color','font-size']:
		if x in styleDict.keys():
			sendDict[x]=styleDict[x]
			del styleDict[x]
	fadeDict['content'][1]['content'][1]['img'].update(styleDict)
	sendDict={'fade':sendDict}
	makeCSS(sendDict)
	CSSCount['fade']=CSSCount['fade']+1
	return fadeDict

def imageMaker(style,content):
	if('flip' in style):
		makeCSS({'flip':{'class':'#flip'+str(CSSCount['flip'])}})
	if('shake' in style):
		makeCSS({'shake':{'class':'#shake'+str(CSSCount['shake'])}})
	if content:
		styleDict={TwoNonCSS[y[:y.find(':')].strip()]:y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')].strip() in TwoNonCSS.keys()]}
		for x in [OneNonCSS[x.strip()] for x in style.split(',') if x.find(':')==-1 and x.strip() in OneNonCSS.keys()]:
			if list(x.keys())[0] in styleDict.keys():
				styleDict[list(x.keys())[0]]=styleDict[list(x.keys())[0]]+' '+list(x.values())[0]
			else:
				styleDict[list(x.keys())[0]]=list(x.values())[0]
		styleDict.update({'src':"img/" + content.strip()})
		currDict={'img':styleDict,'content':{}}
		if('flip' in style):
			currDict={'div':{'id':'flip'+str(CSSCount['flip'])},'content':{1:copy.deepcopy(currDict)}}
			CSSCount['flip']=CSSCount['flip']+1
		if('shake' in style):
			currDict={'div':{'id':'shake'+str(CSSCount['shake'])},'content':{1:copy.deepcopy(currDict)}}
			CSSCount['shake']=CSSCount['shake']+1
		if('enlarge' in style):
			currDict={'div':{'id':'enlarge'+str(CSSCount['enlarge'])},'content':{1:copy.deepcopy(currDict)}}
			makeCSS({'enlarge':{'class':'#enlarge'+str(CSSCount['enlarge']),'width':styleDict['width'],'scale':styleDict['scale']}})
			CSSCount['enlarge']=CSSCount['enlarge']+1
		if('center' in style):
			currDict={'div':{'align':'center'},'content':{1:currDict}}
		return currDict

def linkMaker(style,content):
	if content:
		styleDict={TwoNonCSS[y[:y.find(':')].strip()]:y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')].strip() in TwoNonCSS.keys()]}
		for x in [OneNonCSS[x.strip()] for x in style.split(',') if x.find(':')==-1 and x.strip() in OneNonCSS.keys()]:
			if list(x.keys())[0] in styleDict.keys():
				styleDict[list(x.keys())[0]]=styleDict[list(x.keys())[0]]+' '+list(x.values())[0]
			else:
				styleDict[list(x.keys())[0]]=list(x.values())[0]
		if 'alt' in styleDict.keys():
			styleDict.update({'href':content.strip()})
			tmp=styleDict['alt']
			del styleDict['alt']
			return {'a':styleDict,'content':tmp}
		else:
			styleDict.update({'href':content.strip()})
			return {'a':styleDict,'content':content.strip()}

def listMaker(style,content):
	if content:
		if style:
			styleDict={TwoNonCSS[y[:y.find(':')].strip()]:y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')].strip() in TwoNonCSS.keys() and not(x[x.find(':')+1].strip()=='<')]}
			for x in [OneNonCSS[x.strip()] for x in style.split(',') if x.find(':')==-1 and x.strip() in OneNonCSS.keys()]:
				if list(x.keys())[0] in styleDict.keys():
					styleDict[list(x.keys())[0]]=styleDict[list(x.keys())[0]]+' '+list(x.values())[0]
				else:
					styleDict[list(x.keys())[0]]=list(x.values())[0]
			listType=style.strip()[0]
			if listType=='d':
				listData=[y.strip('\t\n\r* ') for y in content.split('\n')[1:-1]]
				# listData=list(itertools.chain.from_iterable([x.split('**') for x in listData]))
				listDict={}
				for i in range(0,len(listData)):
					if(i%2==0):
						listDict.update({i+1:{'dt':{},'content':listData[i]}})
					else:
						listDict.update({i+1:{'dd':{},'content':listData[i]}})
			else:

				listData=[y.strip('\t\n\r* ') for y in content.split('\n')[1:-1]]
				listDict={}
				for i in range(0,len(listData)):
					listDict.update({i+1:{'li':{},'content':listData[i]}})
			if('terminal' in style):
				if(CSSCount['terminal'] == 1):
					makeCSS({'terminal':{}})
					CSSCount['terminal']=0
				listDict={'div':{'class':'terminal'},'content':{1:listDict}}
			return {listType+'l':styleDict,'content':listDict}

#tableTypes={"avacado":"table table-bordered","durian":"table table-condensed table-hover","pitaya":"table table-striped","cherimoya":"table table-striped table-hover","kiwano":"table table-bordered table-striped table-hover table-condensed"}

def tableMaker(style,content):
	def f(l,t):
		tableDict={}
		for j in range(0,len(l)):
			tmpDict={}
			for i in range(0,len(l[j])):
				if(l[j][i][0]=='*' and l[j][i][-1]=='*'):
					l[j][i]=l[j][i].strip('*')
					tmp=int((i/2)+1)
					if(l[j][i] and l[j][i].count(',')==1):
						l[j][i]=l[j][i].split(',')
						tmptmpDict={tmp:{'td':{'colspan':l[j][i][0].strip(),'rowspan':l[j][i][1].strip()},'content':{}}}
					elif(not l[j][i]):
						tmptmpDict={tmp:{'td':{},'content':{}}}
					else:
						tmptmpDict={tmp:{'td':{'colspan':l[j][i][0].strip()},'content':{}}}
				else:
					tmptmpDict[(i+1)/2]['content']=l[j][i].strip()
					tmpDict.update(tmptmpDict)
					tmptmpDict={}
			tableDict.update({j+1+t:{'tr':{},'content':tmpDict}})
		return tableDict

	if content:
		styleDict={TwoNonCSS[y[:y.find(':')].strip()]:y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')].strip() in TwoNonCSS.keys()]}
		if 'class' in styleDict.keys():
			styleDict['class']=styleDict['class']+' table'
		else:
			styleDict['class']='table'
		for x in [OneNonCSS[x.split()] for x in style.split(',') if x.find(':')==-1 and x.split() in OneNonCSS.keys()]:
			if list(x.keys())[0] in styleDict.keys():
				styleDict[list(x.keys())[0]]=styleDict[list(x.keys())[0]]+' '+list(x.values())[0]
			else:
				styleDict[list(x.keys())[0]]=list(x.values())[0]
		content=content.split('\n')
		r1 = re.compile("(\*[0-9,]*\*)")
		contents = [re.split(r1,x)[1:] for x in content[1:-1]]
		if 'caption' in styleDict.keys():
			captionText=styleDict['caption']
			del styleDict['caption']
			dataDict=f(contents,1)
			dataDict.update({1:{'caption':captionText}})
		else:
			dataDict=f(contents,0)
		return {'table':styleDict,'content':dataDict}

'''
input:- slideshow(type:1){(r){caption}:img,caption:img,img}
output:- dictionary of slideshow
'''
def slideshowMaker(s,i):
	content = i.split(',')
	slideshow_dict = copy.deepcopy(slideshow_carousel)
	elem = copy.deepcopy(slideshow_carousel['content'][2]['content'][1])
	extra = copy.deepcopy(slideshow_carousel['content'][1]['content'][1])
	count=1
	for x in content:
		row =copy.deepcopy(elem)
		extra_this_row = copy.deepcopy(extra)
		if(':' in x):
			row['content'][2]['content'][1]['content']= x.split(':')[0].strip()
			row['content'][1]['img']['src'] = 'img/' + x.split(':')[1].strip()
		else:
			del row['content'][2]
			row['content'][1]['img']['src'] = 'img/' + x.strip()
		
		if(count == 1):
			row['div']['class'] = 'active ' + row['div']['class']
			extra_this_row['li']['class'] = 'active'
		extra_this_row['li']['data-slide-to'] = str(count-1) 
		slideshow_dict['content'][2]['content'][count] = row
		slideshow_dict['content'][1]['content'][count] = extra_this_row
		count=count+1
	return slideshow_dict

def parallaxMaker(s,i):
	if('advanced' in s):
		parallax_dict={'div':{'id':'aparallax'+str(CSSCount['aparallax']),'height':{},'data-stellar-background-ratio':{}},'content':''}
		content=i.strip()
		parallax_dict['div']['background-image']="url('img/"+content+"')"
		for x in s.split(','):
			if(':' in x):
				if(x[:x.find(':')].strip()=='speed'):
					parallax_dict['div']['data-stellar-background-ratio']=x[x.find(':')+1:].strip()
				else:
					parallax_dict['div'][x[:x.find(':')].strip()]=x[x.find(':')+1:].strip()
		if not parallax_dict['div']['height']:
			parallax_dict['div']['height']='678px'
		if not parallax_dict['div']['data-stellar-background-ratio']:
			parallax_dict['div']['data-stellar-background-ratio']='0.5'
		CSSCount['aparallax']=CSSCount['aparallax']+1
		makeJS({'advanced-parallax':{}})
		return parallax_dict
	else:
		parallax_dict = {'div':{'id':'parallax' + str(CSSCount['parallax']) , 'background-image':''} , 'content':''}
		content = i.strip()
		parallax_dict['div']['background-image'] = "url('img/" + content + "')"
		CSSCount['parallax'] = CSSCount['parallax']+1
		makeCSS({'parallax':{'class':'#' + parallax_dict['div']['id']}})
		return parallax_dict

# accordions are drop-down sections of text which are useful when you want to enter a large amount of text
# Currently no styles are implemented for accordion
def accordionMaker(s,i):
	# accordion_dict is the template dictionary for the accordion
	accordion_dict  = {'div':{'id':'accordion'+str(CSSCount['accordion'])},'content':{}}
	CSSCount['accordion'] = CSSCount['accordion']+1
	title_dict = {'button':{'class':'accordion'} , 'content':''}
	text_dict = {'div':{'class':'panel'},'content' : {1 : {'p':{} , 'content' : ''}}}
	CHARACTER_CLASS = ''' \nABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-,.:;'"!@#$%^&(){}[]\|'''
	ELEM = Group(Suppress('*') + Word(CHARACTER_CLASS) + Suppress('**') + Word(CHARACTER_CLASS))
	CONTENT = ZeroOrMore(ELEM)

	lol = CONTENT.parseString(i).asList()

	count = 1
	for line in lol:
		title_elem = copy.deepcopy(title_dict)
		text_elem = copy.deepcopy(text_dict)
		title_elem['content'] = line[0].strip()
		text_elem['content'][1]['content'] = line[1].strip()
		accordion_dict['content'][count] = title_elem
		accordion_dict['content'][count+1] = text_elem
		count = count + 2

	css_for_accordion = {'accordion':{}}
	makeCSS(css_for_accordion)
	makeJS({'accordion':{}})
	return accordion_dict

# No styles are yet implemented for timeline
def timelineMaker(s,i):
	css_for_timeline = {'timeline':{'class':''}}
	timeline_dict = {'div':{'id':''} , 'content':{}}
	timeline_dict['div']['id'] = 'timeline' + str(CSSCount['timeline'])
	CSSCount['timeline'] = CSSCount['timeline'] + 1
	css_for_timeline['timeline']['class'] = '#' + timeline_dict['div']['id']
	makeCSS(css_for_timeline)
	# Just append ' left' or ' right' to elem class
	elem = {'div':{'class':'container'} , 'content':{
		1:{'div':{'class':'content'} , 'content':{
			1:{'h2':{}, 'content' : ''},
			2:{'p':{} , 'content' : ''}}}}}

	CHARACTER_CLASS = ''' \nABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-,.:;'"!@#$%^&(){}[]\|'''
	ELEM = Group(Suppress('*') + Word(CHARACTER_CLASS) + Suppress('**') + Word(CHARACTER_CLASS))
	CONTENT = ZeroOrMore(ELEM)
	lol = CONTENT.parseString(i).asList()
	Left = True;
	count = 1;
	for [u,v] in lol:
		row = copy.deepcopy(elem)
		row['content'][1]['content'][1]['content'] = u
		row['content'][1]['content'][2]['content'] = v
		if (Left):
			row['div']['class'] = row['div']['class'] + ' left'
		else :
			row['div']['class'] = row['div']['class'] + ' right'
		Left = not(Left)
		timeline_dict['content'][count] = row
		count = count + 1
	return timeline_dict

def blockMaker(s,i):
	block_dict = {'div':{'id':''} , 'content':''}
	block_dict['div']['id'] = 'block'+ str(CSSCount['block'])
	CSSCount['block'] = CSSCount['block'] + 1
	block_dict['content'] = i
	css_for_block = {'block':{'class':''}}
	css_for_block['block']['class'] = '#'+ block_dict['div']['id']
	if s:
		s = dictionaryMaker(s)
		for u,v in s.items():
			css_for_block['block'][u] = v;
	makeCSS(css_for_block)
	return block_dict

def skillbarMaker(s,i):
	skillbar_dict = {'div':{'id':''} , 'content':{}}
	skillbar_dict['div']['id'] = 'skillbar' + str(CSSCount['skillbar'])
	CSSCount['skillbar'] = CSSCount['skillbar'] + 1
	bar = {'div':{'class':'container'}, 'content':{1 :{'div':{'class':'skills'} , 'content':''}}}
	css_for_skillbar = {'skillbar':{'class':'' , }}
	css_for_skillbar['skillbar']['class'] = '#' + skillbar_dict['div']['id']
	s = dictionaryMaker(s)
	#eprint(s)
	for u,v in s.items():
		css_for_skillbar['skillbar'][u] = v
	i = i.split(',')
	count = 1
	for pair in i:
		pair = pair.split(':')
		title = pair[0].strip()
		skillbar_dict['content'][count] = {'p':{} , 'content':title}
		count = count + 1
		bar_copy = copy.deepcopy(bar)
		bar_copy['content'][1]['content'] = pair[1].strip()
		bar_copy['content'][1]['div']['class'] = bar_copy['content'][1]['div']['class'] + ' bar' + str(int(count/2))
		css_for_skillbar['skillbar']['.bar' +str(int(count/2))] = pair[1].strip()
		skillbar_dict['content'][count] = bar_copy
		count = count + 1
	makeCSS(css_for_skillbar)
	return skillbar_dict

def checkboxMaker(style,content):
	checkboxDict = {'label':{'id':'checkbox'+str(CSSCount['checkbox'])},'content':{1:'',2:{'input':{'type':'checkbox'},'content':''},3:{'span':{'class':'checkmark'},'content':''}}}
	sendDict={'checkbox':{'class':'#checkbox'+str(CSSCount['checkbox'])}}
	checkboxDict['content'][1]=content
	if('checked' in style):
		checkboxDict['content'][2]['input']['checked']='checked'
		style.replace('checked','') 
	makeCSS(sendDict)
	CSSCount['checkbox']=CSSCount['checkbox']+1
	#print(checkboxDict)
	return checkboxDict

def tooltipMaker(style,content):
	tooltipDict={'div':{'id':'tooltip'+str(CSSCount['tooltip'])},'content':{1:'',2:{'span':{'class':'tooltiptext'},'content':''}}}
	sendDict={'tooltip':{'class':'#tooltip'+str(CSSCount['tooltip'])}}
	styleDict={TwoNonCSS[y[:y.find(':')].strip()]:y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')].strip() in TwoNonCSS.keys()]}
	sendDict['tooltip'].update(styleDict)
	makeCSS(sendDict)
	content=content.split(':')
	tooltipDict['content'][1]=content[0]
	tooltipDict['content'][2]['content']=content[1]
	CSSCount['tooltip'] = CSSCount['tooltip']+1
	return tooltipDict

def chatboxMaker(s,i):
	#eprint(i)
	css_for_chatbox = {'chatbox':{'class':''}}
	chatbox_dict = {'div':{'id':''} , 'content':{}}
	chatbox_dict['div']['id'] = 'chatbox' + str(CSSCount['chatbox'])
	CSSCount['chatbox'] = CSSCount['chatbox'] + 1
	css_for_chatbox['chatbox']['class'] = '#' + chatbox_dict['div']['id'] 
	makeCSS(css_for_chatbox)
	# Just append ' darker' for other color, 'time-right' and 'time-left' class time display
	elem = {'div':{'class':'container'} , 'content':{
		1:{'img':{'src':''} , 'content':''},
		2:{'p':{}, 'content' : ''},
		3:{'span':{'class':''} , 'content' : ''}}}

	CHARACTER_CLASS = ''' \t\nABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-,.:;'"!?@#$%^&(){}[]\|'''
	ELEM = Group(Suppress('*') + Word(CHARACTER_CLASS) + Suppress('**') + Word(CHARACTER_CLASS))
	CONTENT = ZeroOrMore(ELEM)
	lol = CONTENT.parseString(i.strip('\n')).asList()
	last_state = ['left',0]
	count = 1;
	[img1,img2] = ['img/' + i.strip() for i in s.split(',')]
	for [u,v] in lol:
		row = copy.deepcopy(elem)
		u = u.split(',')
		if ('1' in u):
			last_state[1] = 1
			u.remove('1')
		elif ('0' in u):
			last_state[1] = 0
			u.remove('0')
		else:
			last_state[1] = 1 - last_state[1]
		if ('left' in u):
			last_state[0] = 'left'
			u.remove('left')
		elif ('right' in u):
			last_state[0] = 'right'
			u.remove('right')
		elif (last_state[0] == 'left'):
			last_state[0] = 'right'
		else:
			last_state[0] = 'left'
		if (last_state[0] == 'right'):
			row['div']['class'] = row['div']['class'] + ' darker'
		if(last_state[0] == 'right'):
			row['content'][1]['img']['class'] = ' right'
		if (last_state[1] == 0):
			row['content'][1]['img']['src'] = img1
		else:
			row['content'][1]['img']['src'] = img2
		if(last_state[0] == 'left'):
			row['content'][3]['span']['class'] = 'time-right'
		else:
			row['content'][3]['span']['class'] = 'time-left'
		row['content'][3]['content'] = u[0]
		row['content'][2]['content'] = v
		chatbox_dict['content'][count] = row
		count = count + 1
	return chatbox_dict

def alertMaker(s,i):
	alert_dict = {'div':{'id':''} , 'content':{
		1: {'span':{'class':'closebtn', 'onclick':'''this.parentElement.style.display="none" '''} , 'content':'&times;'},
		2:''}}
	alert_dict['content'][2] = i
	alert_dict['div']['id'] = 'alert' + str(CSSCount['alert'])
	s = [x.strip() for x in s.split(',')]
	css_for_alert = {'alert':{'class':'#alert' + str(CSSCount['alert'])}}
	if ('danger' in s):
		css_for_alert['alert']['color'] = '#ed314d'
		s.remove('danger')
	elif ('success' in s):
		css_for_alert['alert']['color'] = '#d1ffa0'
		s.remove('success')
	elif ('warning' in s):
		css_for_alert['alert']['color'] = '#f2ba21'
		s.remove('warning')
	elif ('info' in s):
		css_for_alert['alert']['color'] = '#a16fe8'
		s.remove('info')
	for x in s:
		if(x.find(':') != -1):
			css_for_alert['alert'][x[:x.find(':')]] = x[x.find(':')+1:]
	CSSCount['alert'] = CSSCount['alert'] +1
	makeCSS(css_for_alert);
	return alert_dict

def dictOfStyles(s):
	# This function converts string of style into dictionary with two keys, binary and unary
	# Input -> Output
	# type:type1 , width:300px , height:400px , fade , auto -> {unary : {fade:'' , auto:''} , binary : {type:type1 , width:300px , height : 400px}}
	style_dict = {'unary':{} , 'binary':{}}
	x = [x.strip() for x in s.split(',')]
	for i in x:
		if(i.find(':') != -1):
			key = i[:i.find(':')].strip()
			value = i[i.find(':')+1:].strip()
			style_dict['binary'][key] = value
		else:
			style_dict['unary'][i]=''
	return style_dict

def checkImageExtension(img):
	# The input is string
	# The supported extensions are .jpg, .jpeg, .bmp, .png, .gif
	img = img.strip()
	ext = img[-img[::-1].find('.') - 1:]
	return ((ext == '.png') or (ext == '.jpg') or (ext == '.jpeg') or (ext == '.bmp') or (ext == '.gif'))

def wallpaperMaker(s,i):
	# For type1 wallpaper allowed input for i are
	# Name, Img, Description
	# Img, Name, Description
	# Img, Name
	# Name, Img
	# Img
	styleDict={TwoNonCSS[y[:y.find(':')].strip()]:y[y.find(':')+1:].strip() for y in [x for x in s.split(',') if not(x.find(':')==-1) and x[:x.find(':')].strip() in TwoNonCSS.keys()]}
	if(styleDict['type']=='type1'):
		wallpaper_type1 = {'div':{'class':'container-fluid bg text-center'} , 'content':{}}
		NAME = {'h3':{'class':'margin'} , 'content' : ''}
		IMG = {'img':{'src':'' , 'class':'img-responsive img-circle margin' , 'display':'inline' , 'width':'350' , 'height':'350'} , 'content':''}
		DESCRIPTION = {'h3':{} , 'content' : ''}
		style_dict = dictOfStyles(s)
		css_for_wallpaper = {'wallpaper':{'class':'', 'type':'type1'}}
		wallpaper_type1['div']['id'] = 'wallpaper' + str(CSSCount['wallpaper'])
		css_for_wallpaper['wallpaper']['class'] = '#' + wallpaper_type1['div']['id']
		CSSCount['wallpaper'] = CSSCount['wallpaper']+1
		for key,value in style_dict['binary'].items():
			css_for_wallpaper['wallpaper'][key] = value
		makeCSS(css_for_wallpaper)
		if i.find(',') == -1:
			eprint("Content of wallpaper must have atleast one argument")
		else:
			content = i.split(',',2)
			content = [c.strip() for c in content]
		if checkImageExtension(content[0]):
			arg = len(content)
			IMG['img']['src'] = 'img/' + content[0]
			if arg == 2:
				NAME['content'] = content[1]
				wallpaper_type1['content'][2] = NAME
			if arg == 3:
				NAME['content'] = content[1]
				wallpaper_type1['content'][2] = NAME
				DESCRIPTION['content'] = content[2]
				wallpaper_type1['content'][3] = DESCRIPTION
			wallpaper_type1['content'][1] = IMG
		else:
			NAME['content'] = content[0]
			wallpaper_type1['content'][1] = NAME
			if checkImageExtension(content[1]):
				arg = len(content)
				IMG['img']['src'] = 'img/' +content[1]
				wallpaper_type1['content'][2] = IMG
				if arg == 3:
					DESCRIPTION['content'] = content[2]
					wallpaper_type1['content'][3] = DESCRIPTION
			else:
				DESCRIPTION['content'] = content[1]
				wallpaper_type1['content'][2] = DESCRIPTION
				IMG['img']['src'] = 'img/' + content[2]
				wallpaper_type1['content'][3] = IMG
		return wallpaper_type1
	elif(styleDict['type']=='type2'):
		sendDict={'wallpaper2':{'class':'#wallpaper2'+str(CSSCount['wallpaper2'])}}
		sendDict['wallpaper2'].update(styleDict)
		makeCSS(sendDict)
		content=i.split(':')
		wallpaper_type2={'div':{'id':'wallpaper2'+str(CSSCount['wallpaper2'])},'content':{1:content[1],2:{'div':{'class':'centered'},'content':content[0]}}}
		CSSCount['wallpaper2']=CSSCount['wallpaper2']+1
		return wallpaper_type2


def textfieldMaker(style,content):
	sendDict={TwoNonCSS[y[:y.find(':')].strip()]:y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')].strip() in TwoNonCSS.keys()]}
	textfieldDict={1:{'label':{'for':'textfield'+str(CSSCount['textfield'])},'content':{}},2:{'input':{'id':'textfield'+str(CSSCount['textfield']),'type':'text'},'content':''}}
	if(':' in content):
		textfieldDict[1]['content']=content[:content.find(':')].strip()
		textfieldDict[2]['input']['placeholder']=content[content.find(':')+1:].strip()
	else:
		textfieldDict[1]['content']=content[:content.find(':')].strip()
	sendDict['class']='#textfield'+str(CSSCount['textfield'])
	sendDict={'textfield':sendDict}
	makeCSS(sendDict)
	CSSCount['textfield']=CSSCount['textfield']+1
	return textfieldDict

def passwordfieldMaker(style,content):
	sendDict={TwoNonCSS[y[:y.find(':')].strip()]:y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')].strip() in TwoNonCSS.keys()]}
	passwordfieldDict={1:{'label':{'for':'passwordfield'+str(CSSCount['passwordfield'])},'content':{}},2:{'input':{'id':'passwordfield'+str(CSSCount['passwordfield']),'type':'password'},'content':''}}
	if(':' in content):
		passwordfieldDict[1]['content']=content[:content.find(':')].strip()
		passwordfieldDict[2]['input']['placeholder']=content[content.find(':')+1:].strip()
	else:
		passwordfieldDict[1]['content']=content[:content.find(':')].strip()
	sendDict['class']='#passwordfield'+str(CSSCount['passwordfield'])
	sendDict={'passwordfield':sendDict}
	makeCSS(sendDict)
	CSSCount['passwordfield']=CSSCount['passwordfield']+1
	return passwordfieldDict

def selectMaker(style,content):
	sendDict={TwoNonCSS[y[:y.find(':')].strip()]:y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')].strip() in TwoNonCSS.keys()]}
	selectDict={1:{'label':{'for':'select'+str(CSSCount['select'])},'content':{}},2:{'select':{'id':'select'+str(CSSCount['select'])},'content':{}}}
	selectDict[1]['content']=content[:content.find(':')].strip()
	i=1
	tmpDict={}
	for x in content[content.find(':')+1:].split(','):
		tmpDict.update({i:{'option':{'value':x.strip().lower()},'content':x.strip()}})
		i=i+1
	selectDict[2]['content']=tmpDict
	sendDict['class']='#select'+str(CSSCount['select'])
	sendDict={'select':sendDict}
	makeCSS(sendDict)
	CSSCount['select']=CSSCount['select']+1
	return selectDict

def submitMaker(style,content):
	sendDict={'class':'#submit'+str(CSSCount['submit'])}
	tempDict={y[:y.find(':')].strip():y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1)]}
	for x in [OneNonCSS[x.strip()] for x in style.split(',') if x.find(':')==-1 and x.strip() in OneNonCSS.keys()]:
		for (key,value) in x.items():
			if key in tempDict.keys():
				tempDict[key]=tempDict[key]+' '+value
			else:
				tempDict[key]=value
	sendDict.update(tempDict)
	submitDict={'input':{'type':'submit','value':content.strip(),'id':'submit'+str(CSSCount['submit'])},'content':{}}
	sendDict={'submit':sendDict}
	makeCSS(sendDict)
	CSSCount['submit']=CSSCount['submit']+1
	return submitDict

def galleryMaker(style,content):
	#eprint("gallery!!")
	column=int(style)
	length=int(12/column)
	content=content.split(',')
	rs=''
	count=0
	for obj in content:
		if(':' in obj):
			img=obj.split(':')[1]
			caption=obj.split(':')[0]
			if(count%12==0):
				rs=rs+"grid("+(str(length)+",")*(column-1)+str(length)+")"
			rs=rs+"{"+"block(margin-top:0px,margin-right:0px,padding-right:2px,padding-top:0px){image(width:100%){"+img+"}||(center,h4){"+caption+"|| ||} } }"
			count=(count+length)%12
		else:
			img=obj
			caption="||"
			if(count%12==0):
				rs=rs+"grid("+(str(length)+",")*(column-1)+str(length)+")"
			rs=rs+"{"+"block(margin-top:0px,margin-right:0px,padding-right:2px,padding-top:0px){image(width:100%){"+img+"}||(center,h4){"+caption+"||  }} }"
			count=(count+length)%12
	while(not count%12==0):
		rs=rs+"{}"
		count=count+length
	return rs

def iconbarMaker(style,content):
	iconbarDict={'div':{'id':'iconbar'+str(CSSCount['iconbar'])},'content':{1:{'a':{'href':''},'content':{1:{'i':{'class':'fa fa-'},'content':''}}}}}
	sendDict={'iconbar':{'class':'#iconbar'+str(CSSCount['iconbar'])}}
	tempDict={y[:y.find(':')].strip():y[y.find(':')+1:].strip() for y in [x for x in style.split(',') if not(x.find(':')==-1)]}
	for x in [OneNonCSS[x.strip()] for x in style.split(',') if x.find(':')==-1 and x.strip() in OneNonCSS.keys()]:
		for (key,value) in x.items():
			if key in tempDict.keys():
				tempDict[key]=tempDict[key]+' '+value
			else:
				tempDict[key]=value
	sendDict['iconbar'].update(tempDict)
	makeCSS(sendDict)
	CSSCount['iconbar']=CSSCount['iconbar']+1
	change=copy.deepcopy(iconbarDict['content'][1])
	count=1
	for x in content.split(','):
		name=x.split(':')[0]
		link=x.split(':',1)[1]
		part=copy.deepcopy(change)
		part['a']['href']=link
		if(name in social_icons.keys() ):
			part['content'][1]['i']['class']=part['content'][1]['i']['class']+social_icons[name]
		else:
			part['content'][1]['i']['class']=part['content'][1]['i']['class']+name
		iconbarDict['content'][count]=part
		count=count+1

	#eprint(iconbarDict)
	return iconbarDict



styleFunctions = {
	'image':imageMaker,
	'link':linkMaker,
	'list':listMaker,
	'table':tableMaker,
	'slideshow':slideshowMaker,
	'parallax':parallaxMaker,
	'fade':fadeMaker,
	'card':cardMaker,
	'piechart':piechartMaker,
	'button':buttonMaker,
	'accordion':accordionMaker,
	'timeline':timelineMaker,
	'chatbox':chatboxMaker,
	'checkbox':checkboxMaker,
	'alert':alertMaker,
	'wallpaper':wallpaperMaker,
	'skillbar':skillbarMaker,
	'tooltip':tooltipMaker,
	'textfield':textfieldMaker,
	'passwordfield':passwordfieldMaker,
	'select':selectMaker,
	'submit':submitMaker, 
	'block':blockMaker,
	'gallery':galleryMaker,
	'iconbar':iconbarMaker
}

allowedStyles={
	'height':r'([\d]+[\s]*%$)|([\d]+[\s]*(px|cm|mm|pt)$)',
	'width':r'([\d]+[\s]*%$)|([\d]+[\s]*(px|cm|mm|pt)$)',
	'font-size':r'([\d]+[\s]*(px|cm|mm|pt)$)',
	'align':r'(center$)|(left$)|(right$)',
	'text-align':r'(center$)|(left$)|(right$)',
	'float':r'(center$)|(left$)|(right$)',
	'fade':r'(bottom$)|(left$)|(right$)|(top$)',
	'opacity':r'([01](\.[\d]*)?$)',
	'speed':r'([\d]*(\.[\d]*)?$)',
	'padding':r'([\d]+[\s]*(px|cm|mm|pt)$)',
	'padding-top':r'([\d]+[\s]*(px|cm|mm|pt)$)',
	'padding-bottom':r'([\d]+[\s]*(px|cm|mm|pt)$)',
	'padding-left':r'([\d]+[\s]*(px|cm|mm|pt)$)',
	'padding-right':r'([\d]+[\s]*(px|cm|mm|pt)$)',
	'margin':r'([\d]+[\s]*(px|cm|mm|pt)$)',
	'margin-left':r'([\d]+[\s]*(px|cm|mm|pt)$)',
	'margin-right':r'([\d]+[\s]*(px|cm|mm|pt)$)',
	'border':r'([\d]+[\s]*(px|cm|mm|pt)$)',
	'font-color':r'(\#[a-fA-F0-9]{6}$)|(#[a-fA-F0-9]{3}$)|([a-zA-Z]+$)|(rgb\([\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\)$)',
	'color':r'(\#[a-fA-F0-9]{6}$)|(\#[a-fA-F0-9]{3}$)|([a-zA-Z]+$)|(rgb\([\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\)$)',
	'background-color':r'(#[a-fA-F0-9]{6}$)|(#[a-fA-F0-9]{3}$)|([a-zA-Z]+$)|(rgb\([\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\)$)',
	'dropdown-color':r'(#[a-fA-F0-9]{6}$)|(#[a-fA-F0-9]{3}$)|([a-zA-Z]+$)|(rgb\([\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\)$)',	
	'hover-font-color':r'(\#[a-fA-F0-9]{6}$)|(\#[a-fA-F0-9]{3}$)|([a-zA-Z]+$)|(rgb\([\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\)$)',
	'hover-color':r'(\#[a-fA-F0-9]{6}$)|(\#[a-fA-F0-9]{3}$)|([a-zA-Z]+$)|(rgb\([\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\)$)',
	'dropdown-font-color':r'(\#[a-fA-F0-9]{6}$)|(\#[a-fA-F0-9]{3}$)|([a-zA-Z]+$)|(rgb\([\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\,[\d]{1,3}[\s]*\)$)',
	'symbol':r'(i)|(I)|(A)|(a)|(1)|(square)|(circle)|(disc)|<img[\s\S]*>'
}

def styleMaker(s):
	styleName=s.split('(')[0]
	styleStyle=s.split('(')[1].split(')')[0].replace('\n','')
	styleContent=s.split('(')[1].split(')')[1].strip('{}')
	for x in styleStyle.split(','):
		if (':' in x):
			if (x[:x.find(':')].strip() in TwoNonCSS.keys()):
				if (x[:x.find(':')].strip() in allowedStyles.keys()):
					if not (re.match(allowedStyles[x[:x.find(':')].strip()],x[x.find(':')+1:].strip())):
						if(styleName):
							eprint("In File "+pageName+" Syntax Error: Incorrect Attribute For "+x[:x.find(':')].strip()+" in "+styleName)
						else:
							eprint("In File "+pageName+" Syntax Error: Incorrect Attribute For "+x[:x.find(':')].strip())
	if(not styleName):
		return taggedMaker(styleStyle,styleContent)
	else:
		return makeHTML(styleFunctions[styleName](styleStyle,styleContent))

def gridMaker(p):
	r=re.compile(r'[\n\t ]*\{[^\{\}]*?\}')
	if('{' in p):
		i=p[p.index('{'):].strip()

		gridList=[]
		while(i):
			a=r.match(i).group()
			gridList.append(a.strip()[1:-1])
			i=i.replace(a,"",1)
		sizeList=p.split('(')[1].split(')')[0].split(',')
		rs='<div class="container-fluid row" >'
		sum=0		
		if (len(sizeList)==len(gridList)):
			for i in range(0,len(sizeList)):
				span=sizeList[i]
				if(':' in span):
					span=span.split(':')
					sum=sum+int(span[0])
					if(span[1]=='f'):
						rs=rs+'<div class="col-sm-'+span[0]+'" style="overflow:hidden;" >'
					elif(span[1]=='s'):
						rs=rs+'<div class="col-sm-'+span[0]+'" style="overflow:auto;height:100%;" >'
				else:
					rs=rs+'<div class="col-sm-'+span+'" >'
					sum=sum+int(span)
				content=gridList[i]
				rs=rs+content+'</div>'
			rs=rs+'</div>'
			if(sum==12):
				return rs
			else:
				eprint("Sum of column span must be 12 in Grid")
		else:
			#eprint("Grid arguments not proper")
			return p
	else:
		return p

'''
This function converts dictionaries to html codes.
Note: It is assumed that styles provided are valid
'''
standAlone=['href', 'src', 'class', 'id','data-stellar-background-ratio', 'for', 'value', 'type', 'checked', 'onclick' , 'rel','data-ride','data-slide',  'data-slide-to', 'data-target','align']
Tags={'img':False,'input':False,'label':True,'select':True,'option':True,'br':False,'hr':False,'header':True,'footer':True,'a':True,'table':True,'ul':True,'ol':True,'h1':True,
'h2':True,'td':True,'tr':True,'h3':True,'h4':True,'h5':True,'h6':True,'b':True,'li':True,'ol':True,'i':True,'script':True,'p':True,
'div':True,'span':True,'nav':True,'button':True, 'head':True, 'body':True, 'dl':True, 'dt':True, 'dd':True, 'title':True, 'style':True , 'link':False, 'html':True, 'footer':True}
def makeHTML(d):
	#eprint(d)
	if(isinstance(d,dict)):
		keysList=list(d.keys())
		if(1 in keysList):
			rs=''
			for i in keysList:
				rs=rs + '\n'+makeHTML(d[i])
			return rs
		else:
			keysList.remove('content')
			Tag=keysList[0]
			if Tag in list(Tags.keys()):
				rs="<"+Tag;
				style=''
				for x in d[Tag].keys():
					if(x in standAlone):
						rs=rs+" "+x+"='"+d[Tag][x]+"'"
					else:
						style=style+x+':'+d[Tag][x]+'; '
				if style=='':
					rs=rs+'>'
				else:
					rs=rs+''' style="'''+style+'''">'''
				if Tags[Tag]:
					if(isinstance(d['content'],dict)):
						newKeyList = list(d['content'].keys())
						for i in newKeyList:
							rs=rs+makeHTML(d['content'][i]) + '\n'
					else:
						rs=rs+d['content']
					rs=rs+"</"+Tag+">"
				return rs
	else:
		return d

def makeNavbar(navbar_style,  navbar_content):
	#print (navbar_style)
	navbar_type = findCorrespondingPair(navbar_style, 'type')[1]
	del navbar_style[findCorrespondingPair(navbar_style,'type')[0]]
	css_for_navbar = {'navbar':{}}
	#print (navbar_type)
	css_for_navbar['navbar']['type'] = navbar_type
	css_for_navbar['navbar']['class'] = '#navbar'
	#print (navbar_style)
	#print (css_for_navbar)
	for i in navbar_style:
		#print ("Hi")
		css_for_navbar['navbar'][i[0]] = i[1]
	if (navbar_type == 'orange' or navbar_type == 'flat' or navbar_type == 'indented'):
		#print (css_for_navbar)
		makeCSS(css_for_navbar)
		#print (css_for_navbar)
		navbar_dict = copy.deepcopy(navbar_flat)
		navbar_dict['div']['id'] = 'navbar'
		li_element = copy.deepcopy(navbar_flat['content'][1]['content'][1])
		for i in range(len(navbar_content)):
			row = copy.deepcopy(li_element)
			row['content'][1]['a']['href']  = navbar_content[i][1]
			if i == 0:
				row['li']['class'] = 'active'
			if (isinstance(navbar_content[i][0],list)):
				row['content'][1]['content'] =  navbar_content[i][0][1]
				if(navbar_content[i][0][0] == 'r'):
					row['li']['float'] =  'right'
				else:
					row['li']['float']  =  'left'
			else:
				row['content'][1]['content'] = navbar_content[i][0]
			navbar_dict['content'][1]['content'][i+1] = row
		#print (navbar_dict)
		return navbar_dict 
	elif navbar_type == 'none':
		navbar_dict = copy.deepcopy(navbar_none)
		navbar_dict['content'][1]['content'][1]['content'][1]['content'] = navbar_content[0][1]
		li_element = copy.deepcopy(navbar_none['content'][2]['content'][1])
		drowdown_element = copy.deepcopy(navbar_none['content'][2]['content'][2])
		li_dropdown_element = copy.deepcopy(navbar_none['content'][2]['content'][2]['content'][2]['content'][1])
		for i in range(1,len(navbar_content)):
			row = copy.deepcopy(drowdown_element)
			if (isinstance(navbar_content[i][1] , list)):
				if (isinstance(navbar_content[i][0],list)):
					row['content'][1]['content'][1] = navbar_content[i][0][1]
					### I don't know how to right align in case of bootstrap.
				else:
					row['content'][1]['content'][1] = navbar_content[i][0]
				for j in range(len(navbar_content[i][1])):
					row_row = copy.deepcopy(li_dropdown_element)
					row_row['content'][1]['content'] = navbar_content[i][1][j][0]
					row_row['content'][1]['a']['href'] = navbar_content[i][1][j][1]
					row['content'][2]['content'][j + 1] = row_row
				navbar_dict['content'][2]['content'][i] = row
			elif (isinstance(navbar_content[i][0],list)):
					row['content'][1]['content'] = navbar_content[i][0][1]
					if(navbar_content[i][0][0] == 'r'):
						row['li']['float'] = 'right'
					else:
						row['li']['float'] = 'left'
			else:
					row['content'][1]['content'] =navbar_content[i][0]
			navbar_dict['content'][2]['content'][i] = li_element
		#eprint (navbar_dict)
		return navbar_dict
	elif navbar_type == 'open':
		css_for_navbar['navbar']['id'] = 'navbar'
		makeCSS(css_for_navbar)
		navbar_dict = copy.deepcopy(navbar_open)
		navbar_dict['div']['id'] = 'navbar'
		navbar_dict['div']['class'] = 'navbar'
		li_element = copy.deepcopy(navbar_open['content'][2]['content'][1]['content'][1])
		for i in range(len(navbar_content)):
			row = copy.deepcopy(li_element)
			row['content'][1]['a']['href']  = navbar_content[i][1]
			if i == 0:
				row['li']['class'] = 'active'
			if (isinstance(navbar_content[i][0],list)):
				row['content'][1]['content'] =  navbar_content[i][0][1]
				if(navbar_content[i][0][0] == 'r'):
					row['li']['float'] =  'right'
				else:
					row['li']['float']  =  'left'
			else:
				row['content'][1]['content'] = navbar_content[i][0]
			navbar_dict['content'][2]['content'][1]['content'][i+1] = row
		makeJS({'navbar':{'type':'open'}})
		return navbar_dict
	elif navbar_type == 'breadcrumbs':
		makeCSS(css_for_navbar)
		navbar_dict = copy.deepcopy(navbar_breadcrumbs)
		navbar_dict['div']['id'] = 'navbar'
		li_element = copy.deepcopy(navbar_breadcrumbs['content'][1]['content'][1]['content'][1])
		for i in range(len(navbar_content)):
			row = copy.deepcopy(li_element)
			row['content'][1]['content'][1]['content'] = str(i+1)
			row['content'][1]['a']['href']  = navbar_content[i][1]
			if i == 0:
				row['li']['class'] = 'active'
			if (isinstance(navbar_content[i][0],list)):
				row['content'][1]['content'][2]['content']  = navbar_content[i][0][1]
				#if(navbar_content[i][0][0] == 'r'):
				#	row['li']['float'] =  'right'
				#else:
				#	row['li']['float']  =  'left'
				
				# No align support for breadcrumbs. It beats the purpose
			else:
				row['content'][1]['content'][2]['content']  = navbar_content[i][0]
			navbar_dict['content'][1]['content'][1]['content'][i+1] = row
		return navbar_dict
	elif navbar_type == 'toggle':
		makeCSS(css_for_navbar)
		navbar_dict = copy.deepcopy(navbar_toggle)
		navbar_dict['header']['id'] = 'navbar'
		li_element = copy.deepcopy(navbar_toggle['content'][2]['content'][1])
		for i in range(len(navbar_content)):
			row = copy.deepcopy(li_element)
			row['content'][1]['a']['href']  = navbar_content[i][1]
			#if i == 0:
			#	row['li']['class'] = 'active'
			if (isinstance(navbar_content[i][0],list)):
				row['content'][1]['content']  = navbar_content[i][0][1]
				# No align support for breadcrumbs. It beats the purpose
			else:
				row['content'][1]['content']  = navbar_content[i][0]
			navbar_dict['content'][2]['content'][i+1] = row
		makeJS({'navbar':{'type':'toggle'}})
		return navbar_dict

def cleanUp(l):
	l = [y for y in l if (y != '{' and y != '}' and y != '(' and y != ')' and y!= ',' and y != ':')]
	for i in range(len(l)):
		if isinstance(l[i],list):
			l[i] = cleanUp(l[i])
	return l

def findCorrespondingPair( lol , val):
	for i in range(len(lol)):
		if lol[i][0] == val:
			return [i,lol[i][1]]
		else:
			return False

social_icons = {'facebook':'facebook',
				'fb':'facebook',
				'google':'google',
				'google-plus':'google-plus',
				'reddit':'reddit',
				'email':'envelope',
				'mail':'envelope',
				'github':'github',
				'pinterest':'pinterest',
				'quora':'quora',
				'skype':'skype',
				'youtube':'youtube',
				'instagram':'instagram',
				'slack':'slack',
				'stackoverflow':'stack-overflow',
				'stack-overflow':'stack-overflow',
				'home':'home',
				'phone':'phone',
				'linkedin':'linkedin',
				'twitter':'twitter'}

def makeFooter(footer_style,footer_content):
	footer_type = findCorrespondingPair(footer_style, 'type')[1]
	del footer_style[findCorrespondingPair(footer_style,'type')[0]]
	css_for_footer = {'footer':{'class':'#footer' , 'type':footer_type}}
	for i in footer_style:
		css_for_footer['footer'][i[0]] = i[1]
	makeCSS(css_for_footer)
	if footer_type == 'basic':
		footer_dict = copy.deepcopy(footer_basic)
		footer_dict['footer']['class'] = 'footer'
		sample_li = copy.deepcopy(footer_basic['content'][2]['content'][1])
		company_name = findCorrespondingPair(footer_content,'NAME')
		if (isinstance(company_name,list)):
			footer_dict['content'][3]['content'] = company_name[1]
			del footer_content[company_name[0]]
		motto = findCorrespondingPair(footer_content,'MOTTO')
		if (isinstance(motto,list)):
			footer_dict['content'][1]['content'] = motto[1]
			del footer_content[motto[0]]
		for i in range(len(footer_content)):
			row = copy.deepcopy(sample_li)
			row['a']['href'] = footer_content[i][1]
			row['content'] = footer_content[i][0]
			footer_dict['content'][2]['content'][2*i+1] = row
			if (i != len(footer_content) -1 ):
				footer_dict['content'][2]['content'][2*i+2] = ' · '
		return footer_dict
	elif footer_type == 'social':
		footer_dict = copy.deepcopy(footer_social)
		footer_dict['footer']['id'] = 'footer'
		elem = copy.deepcopy(footer_social['content'][1]['content'][1])
		for i in range(len(footer_content)):
			row = copy.deepcopy(elem)
			row['content'][1]['i']['class'] = "fa fa-" + social_icons[footer_content[i][0].strip()]
			row['a']['href'] = footer_content[i][1].strip()
			footer_dict['content'][1]['content'][i+1] = row
		return footer_dict
	elif footer_type == 'distributed':
		footer_dict = copy.deepcopy(footer_distributed)
		footer_dict['footer']['class'] = 'footer'
		elem_left = copy.deepcopy(footer_distributed['content'][2]['content'][1]['content'][1])
		elem_right = copy.deepcopy(footer_distributed['content'][1]['content'][1])
		company_name = findCorrespondingPair(footer_content,'NAME')
		temp = ""
		if (isinstance(company_name,list)):
			temp = company_name[1]
			del footer_content[company_name[0]]
		del footer_dict['content'][1]['content'][1]
		for i in range(len(footer_content)):
			if(footer_content[i][0] in social_icons):
				row = copy.deepcopy(elem_right)
				row['content'][1]['img']['src'] = 'img/icons/' + footer_content[i][0].strip() +'.png'
				row['a']['href'] = footer_content[i][1].strip()
				new_index_of_insertion = len(footer_dict['content'][1]['content'].keys())
				footer_dict['content'][1]['content'][new_index_of_insertion+1] = row
			else:
				row = copy.deepcopy(elem_left)
				row['content'] = footer_content[i][0].strip()
				row['a']['href'] = footer_content[i][1].strip()
				new_index_of_insertion = len(footer_dict['content'][2]['content'][1]['content'].keys())
				footer_dict['content'][2]['content'][1]['content'][new_index_of_insertion+1] = row
				footer_dict['content'][2]['content'][1]['content'][new_index_of_insertion+2] = ' · '
		to_remove = max(footer_dict['content'][2]['content'][1]['content'].keys())
		footer_dict['content'][2]['content'][2] = temp
		del footer_dict['content'][2]['content'][1]['content'][to_remove]
		return footer_dict
	elif footer_type == 'distributed_contact':
		footer_dict = copy.deepcopy(footer_distributed_contact)
		print (footer_dict)
	elif footer_type == 'distributed_search':
		footer_dict = copy.deepcopy(footer_distributed_search)
		print (footer_dict)
	elif footer_type == 'distributed_phone_address':
		footer_dict = copy.deepcopy(footer_distributed_phone_address)
		print (footer_dict)

def parseAbstractElement(c):
	PAIR_1 = Word(alphas) + ':' + Word(printables)
	PAIR_2 = Group('(' + Word(alphas , max= 1) + ')' + '{' + Word(alphas) + '}') +':' + Word(printables)
	PAIR_3 = Word(alphas) +':' + Group('{' + OneOrMore(Group(PAIR_1)) +'}')
	PAIR_4 = Group('(' + Word(alphas , max= 1) + ')' + '{' + Word(alphas)  + '}') +':' + Group('{' +  OneOrMore(Group(PAIR_1)) +'}')

	PAIR = Group(PAIR_4 | PAIR_3 | PAIR_2 | PAIR_1)

	#PAIR_3.parseString(' Resume: { onepage : a twopage : b } ').pprint()

	STYLE_1 = Group(Word("abcdefghijklmnopqrstuvwxyz-") + ':' + Word('abcdefghijklmnopqrstuvwxyz-#0123456789(,)'))
	STYLE_2 = Word(alphas)

	STYLE = STYLE_1 + ZeroOrMore(',' + STYLE_1)

	#STYLE.parseString(' type : orange  color:rgb(120,34,76)  font-color : #ef123c ').pprint()

	CONTENT = OneOrMore(PAIR)

	#CONTENT.parseString('Home : www.google.com About : http://www.parser.c..s.s (r){Contact} : Me.ccom').pprint()

	ABSTRACT = Word(alphas) + Group('(' + STYLE + ')') + Group('{' + CONTENT + '}')

	CONFIG = OneOrMore(ABSTRACT)
	config_parsed = CONFIG.parseString(c).asList()
	#eprint(config_parsed)
	return config_parsed

def p_main(p):
    'main : head body'
    p[0]=p[1]+p[2]

def p_head(p):
    '''head : head keyword
            | head NEWLINE
            |
    '''
    if(len(p)==3):
        p[0]=p[1]+p[2]
    else:
        p[0]=''

def p_body(p):
    '''body : body style
            | body REST
            | body newline
            | body pre
            | body code
            | body fakekeyword
            | body hrule
            | body grid
            |
    '''
    if(len(p)==3):
        p[0]=p[1]+p[2]
    else:
        p[0]=''

def p_pre(p):
	'''pre : PRE 
		   |  
	'''
	if(len(p)==2):
		if (p[1][1:6] == 'latex'):
			p[0]="<div lang='latex'>\n"+p[1][:-2][9:].replace('\n','@$$@').replace('(','^**^').replace(')','#!!#').replace('{','&--&').replace('}','+==+')+"\n</div>"
		else:
			p[0]="<pre>"+p[1][:-2][7:].replace('\n','@$$@').replace('(','^**^').replace(')','#!!#').replace('{','&--&').replace('}','+==+').replace('-----','!@#$%^&') +"</pre>"
	else:
		p[0]=''

def p_code(p):
	'''code : CODE
		   |
	'''
	if(len(p)==2):
		p[0]="<code>"+p[1][:-2][8:].replace('\n','@@@@').replace('(','^**^').replace(')','#!!#').replace('{','&--&').replace('}','+==+')+"</code>"
	else:
		p[0]=''

def p_style(p):
    'style : STYLE'
    p[0]=styleMaker(p[1])

def p_newline(p):
	'newline : NEWLINE'
	global LineNumber
	LineNumber=LineNumber+1
	p[0]="\n"

def p_hrule(p):
	'hrule : HRULE'
	p[0]="<hr>"

def p_grid(p):
	'grid : GRID'
	p[0]=gridMaker(p[1])

def p_keyword(p):
    'keyword : KEYWORD'
    if(p[1][0:3]=="###"):
        p[0]=p[1]
    else:
        p[0]="###"+p[1]

def p_fakekeyword(p):
	'fakekeyword : KEYWORD'
	p[0]=p[1]

parser=yacc.yacc()

###########################################################################
# This Part Applies Above Grammar On The File
###########################################################################

main_dict = {'html':{} , 'content':{ 
		1:{'head':{} , 'content':{
			1:{'title':{} , 'content' : ''},
			6:{'style':{} , 'content' : ''},
			5:{'link':{'rel':'stylesheet', 'href':'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'} , 'content':''},
			2:{'link':{'rel':"stylesheet" ,'href':"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"}, 'content':''},
			4:{'link':{'rel':'stylesheet' ,'href':'//netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css'} , 'content':''},
			3:{'link':{'rel':'stylesheet', 'href':'css/style.css'} , 'content':''},
			7:{'script':{'src':'https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js'} , 'content' : ''},
			8:{'script':{'src':'../layout/parallax/jquery.stellar.js'} , 'content' : ''},
			9:{'script':{'src':'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'} , 'content' : ''},
			10:{'script':{'src':'http://latex.codecogs.com/latexit.js' , 'type':'text/javascript'} , 'content':''},
		}} , 
		2:{'body':{} , 'content':{
			1:'',
			2:'',
			3:''
}}}}

global_navbar = {}
global_footer = {}
page_dict = {}
pageName=''
def makeJS(d):
	global page_dict
	element = list(d.keys())[0]
	if ('type' in list(d[element].keys())):
		filename = 'layout/JS/' + element + '_' + d[element]['type'] + '.js'
	else:
		filename = 'layout/JS/' + element + '.js'
	f = open(filename)
	f = f.read()
	count = len(list(page_dict['content'][2]['content'].keys()))
	page_dict['content'][2]['content'][count+1] = {'script':{} , 'content':f}

def main():
	global main_dict
	global page_dict
	global pageName
	page_list = [os.fsdecode(pages) for pages in os.listdir('pages/') if os.fsdecode(pages).endswith('.sm')]
	page_list.sort()
	con = open(os.fsdecode('config.sm'))
	c = con.read()
	c = parseAbstractElement(c)
	if('navbar' in c):
		index_navbar = c.index('navbar')
	else:
		eprint("No rule for navigation bar in config.sm")
		sys.exit()
	#print (index_navbar)
	if('footer' in c):
		index_footer = c.index('footer')
	else:
		eprint("No rule for footer in config.sm")
		sys.exit()
	c = cleanUp(c)
	global_navbar = makeNavbar(c[index_navbar+1],c[index_navbar+2])
	global_footer = makeFooter(c[index_footer+1],c[index_footer+2])
	for page in page_list:
		pageName=page
		page_dict = copy.deepcopy(main_dict)
		page_file = open(os.fsdecode('pages/') + page)
		b=page_file.read()
		while(re.search(r'('+'|'.join(styles)+')?\([^\(\)\{\}]*?\)\{[^\(\)\{\}]*?\}',b)):
			b=parser.parse(b.strip())
			b=b.split("<br>")
			b="<br>\n".join(b)
		b=b.replace('@$$@','\n').replace('^**^','(').replace('#!!#',')').replace('&--&','{').replace('+==+','}').replace('@@@@','<br>').replace('!@#$%^&','-----')
		page_dict['content'][2]['content'][1] = global_navbar
		page_dict['content'][2]['content'][3] = global_footer
		body_content = ""
		style_content = []
		for i in b.split('\n'):
			if(i.find('###') != -1):
				if(i.find('title') != -1):
					page_dict['content'][1]['content'][1]['content'] = i[i.find(':')+1:]
				elif (i.find('nonavbar') != -1):
					del page_dict['content'][2]['content'][1]
				elif (i.find('nofooter') != -1):
					del page_dict['content'][2]['content'][3]
				else:
					style_content.append(i[i.find('###') + 3:])
			else:
				body_content = body_content + i + '\n'
		style_content = 'body {\n' + ';\n'.join(style_content) + ';\n}'
		page_dict['content'][1]['content'][6]['content'] = style_content
		page_dict['content'][2]['content'][2] = body_content.replace('||','<br>\n')
		output_file_name = page.split('.')[0]
		output_file = open('site/' + output_file_name + '.html', 'w')
		output_file.write(makeHTML(page_dict))
		output_file.close()
		page_dict = {}
		LineNumber = 1

main()
