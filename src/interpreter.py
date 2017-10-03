import re,itertools
import copy
from sys import argv
short_syntax = {'r' : 'right' , 'l' : 'left','c':'center'}
import ply.yacc as yacc
from lexer import tokens,styles,keywords
script , pagefile , configfile = argv




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


'''
Boolean function which returns true if the keyword given goes inside style=""

TODO Add an exhaustive list of keywords
'''
def isContained(s):
	keywords = {'id':False , 'href':False , 'class':False , 'width':True , 'height':True , 'background-color':True , 'font-size':True , 'float':True}
	return keywords[s]

'''
Input
> dictionary of attributes

Example
{class:"a" , width:10px , height:30px , href:url ..} -> 'class = "a" style = "width:10px;height:30px;" href=url'

Types of keywords
href, class -> Standalone
width, height, font-size, background-color ->Contained Inside style

We may need a more generic function that this at later point of time. !!
'''
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


'''
This function is used to make container elements like
<html>...</html>
<body>...</body>
<div>...</div>
<table>...</table>

This should be a generic function, to be used for most of the HTML generation.

Input (dictionary,bool) -> Output (string)
{type:attributes , content:"Inside"}

If newline is True the output is
	<type>
		Inside
	</type>
Else
	<type>Inside</type>


Examples

Input {a:{href:url} , content:Text}
Output <a href=url>Text</a>

Input {li:{class:"active"} , content:<a href=url>Text</a>}
Output <li class="active"><a href=url>Text</a></li>

Input {ul:{} , content:<li class="active"><a href=url>Text</a></li>}
Output 
<ul>
	<li class="active"><a href=url>Text</a></li>
</ul>

Input {div:{class=navbar} content:<ul>\n<li class="active"><a href=url>Text</a></li>\n</ul>}
Output
<div class="navbar">
	<ul>
		<li class="active"><a href=url>Text</a></li>
	</ul>
</div>

There we have our navbar complete using this function recursively.
'''
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

'''
Checks whether type matches any of the predefined type and the processes the content corresponding to it
If type is none then user can user other button, drop-down etc of bootstrap
'''

# POWERFUL FUNCTION
def recursiveBuild(dictionary):
	container_name = list(dictionary.keys())
	if not(isinstance(dictionary['content'],dict)):
		return ContainerElement(dictionary, False)
	else:
		inner = recursiveBuild(dictionary['content'])
		dictionary['content'] = inner
		return ContainerElement(dictionary,True);

# MOST POWERFUL FUNCTION
def modifyDictionary(d , path , newvalue):
	if(len(path) == 1):
		d[path[0]] = newvalue
		return d
	else:
		return modifyDictionary(d[path[0]], path[1:] ,newvalue)

ltaggedStyles={"bold":"b","h2":"h2","h1":"h1","h3":"h3","h4":"h4","h5":"h5","h6":"h6","italic":"i","center":"center"}

def taggedMaker(style,content):
    if(not style):
        return content
    else:
        style=style.split(',')
        ltagged=[]
        htagged=[]
        for x in style:
            if(':' in x):
                htagged.append(x)
            else:
                ltagged.append(x)
        if(ltagged and htagged):
            htagged=';'.join(htagged)+';'
            ltaggedStart=''.join(['<'+ltaggedStyles[x]+'>' for x in ltagged])
            ltaggedEnd=''.join(['</'+ltaggedStyles[x]+'>' for x in ltagged[::-1]])
            return "<div style=\""+htagged+"\">"+ltaggedStart+content+ltaggedEnd+"</div>"
        elif(ltagged):
            ltaggedStart=''.join(['<'+str(ltaggedStyles[x])+'>' for x in ltagged])
            ltaggedEnd=''.join(['</'+str(ltaggedStyles[x])+'>' for x in ltagged[::-1]])
            return ltaggedStart+content+ltaggedEnd
        elif(htagged):
            htagged=';'.join(htagged)+';'
            return "<div style=\""+htagged+"\">"+content+"</div>"

TwoNonCSS={'class':'class','id':'id','text':'alt','download':'download','border':'border','caption':'caption','cursor':'cursor','width':'width','height':'height','align':'align','opacity':'opacity','cursor':'cursor','symbol':'type','background-color':'background-color'}
OneNonCSS={'rounded':{'class':'img-rounded'},'circle':{'class':'img-rounded'},'download':{'download':'Untitled_File'},'indented':{'list-style-position':'inside'},'striped':{'class':'striped'},'bordered':{'class':'bordered'},'condensed':{'class':'condensed'},'hover':{'class':'hover'}}
CSS={'card':[1,1],'fade':[2,1]}

def cardMaker(d,s):
	cardDict={'div':{'class':'polaroid'+str(CSS['card'][1])},'content':{1:{},2:{'div':{'class':'polaroid-container'+str(CSS['card'][1])},'content':{1:{'p':{},'content':{}}}}}}
	cardDict['content'][1]=d
	cardDict['content'][2]['content'][1]['content']=s[s.find(':')+1:]
	CSS['card'][1]=CSS['card'][1]+1
	return cardDict

def fadeMaker(d,s):
	fadeDict={'div':{'class':'fade-container'+str(CSS['fade'][1])},'content':{1:{},2:{'div':{'class':'fade-overlay'+str(CSS['fade'][1])},'content':{1:{'div':'fade-text'+str(CSS['fade'][1])},'content':{}}}}}
	if 'class' in d['img'].keys():
		d['img']['class']=d['img']['class']+' fade-image'+str(CSS['fade'][1])
	else:
		d['img']['class']='fade-image'+str(CSS['fade'][1])
	fadeDict['content'][1]=d
	fadeDict['content'][2]['content'][1]['content']=s[s.find(':')+1:]
	CSS['fade'][1]=CSS['fade'][1]+1
	return fadeDict

CodeDict={'card':cardMaker,'fade':fadeMaker}

def imageMaker(style,content):
	if content:
		styleDict={TwoNonCSS[y[:y.find(':')]]:y[y.find(':')+1:] for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')] in TwoNonCSS.keys()]}
		for x in [OneNonCSS[x] for x in style.split(',') if x.find(':')==-1 and x in OneNonCSS.keys()]:
			if list(x.keys())[0] in styleDict.keys():
				styleDict[list(x.keys())[0]]=styleDict[list(x.keys())[0]]+' '+list(x.values())[0]
			else:
				styleDict[list(x.keys())[0]]=list(x.values())[0]
		extraDict={y:CSS[y[:y.find(':')].split('-')[0]] for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')].split('-')[0] in CSS.keys()]}
		styleDict.update({'src':content})
		currDict={'img':styleDict,'content':{}}
		for cssElem in sorted(extraDict,key=extraDict.__getitem__,reverse=True):
			currDict=CodeDict[cssElem[:cssElem.find(':')].split('-')[0]](currDict,cssElem)
		return currDict

def linkMaker(style,content):
	if content:
		if style:
			styleDict={TwoNonCSS[y[:y.find(':')]]:y[y.find(':')+1:] for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')] in TwoNonCSS.keys()]}
			for x in [OneNonCSS[x] for x in style.split(',') if x.find(':')==-1 and x in OneNonCSS.keys()]:
				if list(x.keys())[0] in styleDict.keys():
					styleDict[list(x.keys())[0]]=styleDict[list(x.keys())[0]]+' '+list(x.values())[0]
				else:
					styleDict[list(x.keys())[0]]=list(x.values())[0]
			styleDict.update({'href':content})
			if(style[:style.find(',')] not in OneNonCSS.keys() and ':' not in style[:style.find(',')]):
				return {'a':styleDict,'content':style[:style.find(',')]}
			else:
				return {'a':styleDict,'content':content}
		else:
			return {'a':{'href':content},'content':content}

def listMaker(style,content):
	if content:
		if style:
			styleDict={TwoNonCSS[y[:y.find(':')]]:y[y.find(':')+1:] for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')] in TwoNonCSS.keys() and not(x[x.find(':')+1]=='<')]}
			for x in [OneNonCSS[x] for x in style.split(',') if x.find(':')==-1 and x in OneNonCSS.keys()]:
				if list(x.keys())[0] in styleDict.keys():
					styleDict[list(x.keys())[0]]=styleDict[list(x.keys())[0]]+' '+list(x.values())[0]
				else:
					styleDict[list(x.keys())[0]]=list(x.values())[0]
			listType=style.strip()[0]
			if listType=='d':
				listData=[y[1:].strip('* ') for y in content.split('\n')[1:-1]]
				listData=list(itertools.chain.from_iterable([x.split('**') for x in listData]))
				listDict={}
				for i in range(0,len(listData)):
					if(i%2==0):
						listDict.update({i+1:{'dt':{},'content':listData[i]}})
					else:
						listDict.update({i+1:{'dd':{},'content':listData[i]}})
			else:
				listData=[y[1:].strip() for y in content.split('\n')[1:-1]]
				listDict={}
				for i in range(0,len(listData)):
					listDict.update({i+1:{'li':{},'content':listData[i]}})
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
						tmptmpDict={tmp:{'td':{'colspan':l[j][i][0],'rowspan':l[j][i][1]},'content':{}}}
					elif(not l[j][i]):
						tmptmpDict={tmp:{'td':{},'content':{}}}
					else:
						tmptmpDict={tmp:{'td':{'colspan':l[j][i][0]},'content':{}}}
				else:
					tmptmpDict[(i+1)/2]['content']=l[j][i]
					tmpDict.update(tmptmpDict)
					tmptmpDict={}
			tableDict.update({j+1+t:{'tr':{},'content':tmpDict}})
		return tableDict

	if content:
		styleDict={TwoNonCSS[y[:y.find(':')]]:y[y.find(':')+1:] for y in [x for x in style.split(',') if not(x.find(':')==-1) and x[:x.find(':')] in TwoNonCSS.keys()]}
		if 'class' in styleDict.keys():
			styleDict['class']=styeDict['class']+' table'
		else:
			styleDict['class']='table'
		for x in [OneNonCSS[x] for x in style.split(',') if x.find(':')==-1 and x in OneNonCSS.keys()]:
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

styleFunctions={'image':imageMaker,'link':linkMaker,'list':listMaker,'table':tableMaker}

def styleMaker(s):
    # styleName=re.search(r'(.*?)\(',s).group(1)
    # styleStyle=re.search(r'\((.*?)\)',s).group(1)
    # styleContent=re.search(r'\{(.*?)\}',s).group(1)
    # s=s.replace('\n','')
    styleName=s.split('(')[0]
    styleStyle=s.split('(')[1].split(')')[0].replace('\n','')
    styleContent=s.split('(')[1].split(')')[1].strip('{}')
    # styleStyle=styleStyle.replace(',',';')
    if(not styleName):
        return taggedMaker(styleStyle,styleContent)
    else:
    	return makeHTML(styleFunctions[styleName](styleStyle,styleContent))

'''
input:- slideshow(type:1){(r){caption}:img,caption:img,img}
output:- dictionary of slideshow
'''
def slideshowMaker(i):
	type=i.split('(')[1].split(')')[0].split(':')[1]
	content=re.match(r'slideshow\(.*?\)\{(.*)\}',i).group(1).split(',')
	if content:
		d=copy.deepcopy(slideshow_button)
		i=1
		Slides=copy.deepcopy(d[1]['content'][1])
		for x in content:
			x.strip('}')
			mySlides=copy.deepcopy(Slides)
			if(':' in x):
				mySlides['content'][2]['img']['src']="img/"+x.split(':')[1]
				mySlides['content'][1]['content']=str(i)+" / "+str(len(content))
				if('(' in x):
					mySlides['content'][3]['div']['text-align']=short_syntax[x.split('(')[1].split(')')[0]]
					mySlides['content'][3]['content']=x.split(':')[0].split(')')[1].strip('{}')
				else:
					mySlides['content'][3]['content']=x.split(':')[0]
			else:
				mySlides['content'][2]['img']['src']="img/"+x
				mySlides['content'][1]['content']=str(i)+" / "+str(len(content))
			d[1]['content'][i]=mySlides
			i=i+1
		return d
'''
This function converts dictionaries to html codes.
Note: It is assumed that styles provided are valid
'''
standAlone=['href', 'src', 'class', 'id']
Tags={'img':False,'br':False,'hr':False,'header':True,'footer':True,'a':True,'table':True,'ul':True,'ol':True,'h1':True,'h2':True,'td':True,'tr':True,'h3':True,'h4':True,'h5':True,'h6':True,'b':True,'li':True,'ol':True,'i':True,'script':True,'div':True,'span':True,'nav':True,'button':True}
def makeHTML(d):
	if(isinstance(d,dict)):
		keysList=list(d.keys())
		if(1 in keysList):
			rs=''
			for i in range(1,len(keysList)+1):
				rs=rs+makeHTML(d[i])
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
				if Tags[Tag]	:
					if(isinstance(d['content'],dict)):
						for i in range(0,len(list(d['content'].keys()))):
							rs=rs+makeHTML(d['content'][i+1])
					else:
						rs=rs+d['content']
					rs=rs+"</"+Tag+">"
				return rs
	else:
		return d


def makeNavbar(list_of_tuples):
	#simple_navs = ['orange' , 'flat' , 'indented' , 'wrap' , 'toogle' , 'open' , 'breadcrumbs']
	fixed = {'div':{'id':'cssmenu'}, 'content':{'ul':{} , 'content':'@@@@' } }
	list_element = {'li':{}, 'content':{'a':{'href':'$$$$$'} ,'content':'#####'}}
	#sub_list = {'ul':{} , 'content':{'li':{} , 'content':{'a':{'href':'$$$$$'}, 'content':'#####' } } }
	final_code = ""
	for (index,(i,j)) in enumerate(list_of_tuples):
		# print (index, i , j) #
		# i can be Home or (r){Home} or (l){Home}
		# j can be url or {a:url , b:url}
		code_for_this_pair = ""
		dropdown_code = ""
		copy_list_element = list_element.copy()
		if (index == 0):
			copy_list_element = filler(copy_list_element,['li', 'class'] ,'active')

		matchObj2 = re.match( r'{(.*)}',j, re.M|re.I)
		# print(copy_list_element) #
		if matchObj2:
			print ("Mathched Part 2")
			sub_links = listoftupleMaker(str(matchObj2.group(2)))
			str_dropdown = ""
			for (x,y) in sub_links:
				copy_sub_list = list_element.copy()
				copy_sub_list = filler(copy_sub_list , [ 'content' , 'a' , 'href'] , y)
				copy_sub_list = filler(copy_sub_list , [ 'content' , 'content' ] , x)
				str_dropdown = str_dropdown + recursiveBuild(copy_sub_list) + '\n'
			dropdown_code = content_code + ContainerElement({'ul':{} , 'content':str_dropdown}) + '\n'
			copy_list_element = filler(copy_list_element,['content' , 'a' , 'href'] , '#')
		else:
			copy_list_element = filler(copy_list_element,['content' , 'a' , 'href'] , j)

		matchObj1 = re.match( r'\((.*)\)[ \t]*{.*}',i,re.M|re.I)
		# print(copy_list_element) #
		if matchObj1:
			print ("Mathched Part 1")
			style = str(matchObj1.group(1))
			text = str(matchObj1.group(2))
			style = style.strip()
			if (short_syntax.keys().find(style) != -1):
				copy_list_element = filler(copy_list_element,['content', 'content'],ContainerElement({'span':short_syntax[style] , 'content':text},False) + dropdown_code)
			else:
				copy_list_element = filler(copy_list_element,['content', 'content'],text + dropdown_code)
		else:
			copy_list_element = filler(copy_list_element,['content', 'content'],i + dropdown_code)

		print(copy_list_element) #

		final_code = final_code + recursiveBuild(copy_list_element) + '\n'

		print(final_code) #

	fixed = filler(fixed, ['content' , 'content'] ,final_code)
	return recursiveBuild(fixed)

'''
FOOTERS

TYPE:basic

footer(type:basic){
	MOTTO:
	Home:
	Blog:
	Pricing:
	About:
	FAQ:
	LAST:
}

TYPE:distributed

footer(type:distributed){
	Home:
	Blog:
	Pricing:
	About:
	Contact:
	NAME:
	FACEBOOK:
	TWITTER:
	GITHUB:
	GOOGLE+:
}

TYPE:distributed_phone_address

footer(type:distributed_phone_address){
	Home:
	Contact:
	Blog:
	Pricing:
	ADDRESS:
	PHONE:
	EMAIL:
	FACEBOOK:
	GITHUB:
	LINKEDIN:
}

TYPE:distributed_search

footer(){
	Home:
	Blog:
	Pricing:
	Faq:
}


TYPE:distributed_contact{
	Home:
	Contact:
	Blog:
	Faq:
	FACEBOOK:
	LINKEDIN:
	TWITTER:
	GITHUB:
}

TYPE:social

footer(social){
	FACEBOOK:
	LINKEDIN:
	GITHUB:
	TWITTER:
}
'''

def makeFooter():
	matchObj = re.match(r'.*footer.*\((.*)\){(.*)}' , line , re.DOTALL)
	if matchObj:
		#print (matchObj.group(0))
		#print (matchObj.group(1))
		#print (matchObj.group(2))
		footer_style = str(matchObj.group(1))
		footer_style = "".join(footer_style.split())
		print(footer_style)
		footer_content = matchObj.group(2)
		footer_content = [t.strip() for t in footer_content.strip('\n').split('\n')]
		footer_content = [(temp[:temp.find(':')].strip(),temp[temp.find(':')+1:].strip()) for temp in footer_content]
		print(footer_content)
		footer_type = footer_style[footer_style.find(':')+1:]
		print(footer_type)
		if footer_type == 'basic':
			footer_dict = copy.deepcopy(footer_basic)
			for (i,j) in footer_content:
				if(i == 'MOTTO'):
					modifyDictionary(footer_dict, ['content' , 1 , 'content'] , j)
				elif (i == 'NAME'):
					modifyDictionary(footer_dict, ['content' , 3 , 'content'] , j)
				else:
					sample_li = copy.deepcopy(footer_dict['content'][2]['content'][1])
					modifyDictionary(sample_li,['a','href'] , j)
					modifyDictionary(sample_li , ['content'] , i)
					modifyDictionary(footer_dict, ['content' , 2 , 'content' , footer_content.index((i,j))+1], sample_li)

			print (footer_dict)
		elif footer_type == 'social':
			footer_dict = copy.deepcopy(footer_social)
		elif footer_type == 'distributed':
			footer_dict = copy.deepcopy(footer_distributed)
			print (footer_dict)
		elif footer_type == 'distributed_contact':
			footer_dict = copy.deepcopy(footer_distributed_contact)
			print (footer_dict)
		elif footer_type == 'distributed_search':
			footer_dict = copy.deepcopy(footer_distributed_search)
			print (footer_dict)
		elif footer_type == 'distributed_phone_address':
			footer_dict = copy.deepcopy(footer_distributed_phone_address)
			print (footer_dict)

		footer_content = matchObj.group(2)
		footer_content = [t.strip() for t in footer_content.strip('\n').split('\n')]
		print(footer_content)

	else:
		print ("No Match !")


'''
This function parses abstract element and converts it into dictionary / listoftuple

'''

def parseAbstractElement(s):
	matchObj = re.match( r'^[ \t]*navbar[ \t]*\((.*)\)[ \t]*{(.*)}', s, re.M|re.I)
	if matchObj:
		print ("matchObj.group(1) : ", matchObj.group(1))
		print ("matchObj.group(2) : ", matchObj.group(2))
		paren = str(matchObj.group(1))
		braces = str(matchObj.group(2))
		braces = listoftupleMaker(braces);
		return makeNavbar(braces)
	else:
		print ("No match!!")

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
            | body fakekeyword
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
        p[0]="<pre>"+p[1][:-2][7:].replace('\n','@$$@').replace('(','^**^').replace(')','~!!~').replace('{','&--&').replace('}','+==+')+"</pre>"
    else:
        p[0]=''

def p_style(p):
    'style : STYLE'
    p[0]=styleMaker(p[1])

def p_newline(p):
    'newline : NEWLINE'
    p[0]="<br>"

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


a=open(pagefile)
b=a.read()
while(re.search(r'('+'|'.join(styles)+')?\([^\(\)\{\}]*?\)\{[^\(\)\{\}]*?\}',b)):
    b=parser.parse(b.strip())
b=b.split("<br>")
b="<br>\n".join(b)
b=b.replace('@$$@','\n').replace('^**^','(').replace('~!!~',')').replace('&--&','{').replace('+==+','}')
print(b)

# def makePage():
# 	config = open(configfile)
# 	page = open(pagefile)
# 	l_c = config.readlines()
# 	l_p = page.readlines()
# 	navbar = ""
# 	footer = ""
# 	content = ""
# 	title = ""
# 	infile_css = ""
# 	for i in l_c:
# 		temp = parseAbstractElement(i)
# 		if(temp[0] == 'navbar'):
# 			navbar = temp
# 		elif(temp[0] == 'footer'):
# 			footer = temp
# 	for i in l_p:
# 		if(i[0:3] == '###'):
# 			if(i.count('title') == 1):
# 				title = i[i.find(':') + 1:]
# 			elif(i[3:].split(':')[0].strip() in keywords):
# 				infile_css = infile_css + i[3:].strip('\n')+';\n'
# 			else:
# 				content=content+i
# 		else:
# 			content = content + i
# 	print ("<html>")
# 	print ("<head>")
# 	print ("<title>" + title + "</title>")
# 	print ('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">')
# 	print ("<link rel=\"stylesheet\" href=\"./css/style.css\">")
# 	print ("<style>")
# 	print ("body {")
# 	print (infile_css + "}")
# 	print ('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>')
# 	print ('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>')
# 	print ("</style>")
# 	print ("</head>")
# 	print ("<body>")
# 	#print (makeNavbar(navbar[1],'layout/navbar.html'))
# 	print (content)
# 	print (makeFooter(footer[1], 'layout/footer.html'))
# 	print ("</body>")
# 	print ("</html>")

# line_from_config = 'navbar(type1){Home:{a:alpha,b:beta},About:about.com,Contact:contact.org,Blog:blog.com}'
# print (parseAbstractElement(line_from_config))
