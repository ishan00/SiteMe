import copy
'''
	This file creates the css file corresponding to each file in pages
	The files are named like <page_name>.siteme -> <page_name>.css and placed inside the css folder of site

	Input (Some features will be implemented later yet I have written them in input for consistency)
	{
		navbar : { type : type1 , class : class_name }
		header : { type : type2 , class : class_name }
		footer : { type : type3 , class : class_name }
		table  : { type : type4 , class : class_name , style : {border: val , background-color : color ,  alternate : color , width : 100px ,padding : val} }
		slideshow : { type : carousel , class : class_name }
		grid : { type : type1 , class : class_name , size : (a,b) , content : { {img, title , button , description} * (ab times) }  }
		cover : { type : type2 , class : class_name , content : {img : path , title :  , description : short_description } } 
	}
'''
navbarDict={'$CLASS$':'.navbar','$COLOR$':'#f96e5b','$FONT-COLOR$':'#ffffff','$FONT-SIZE$':'14px','$HOVER-COLOR$':'#ffffff','$HOVER-FONT-COLOR$':'#333333','$DROPDOWN-COLOR$':'none','$DROPDOWN-FONT-COLOR$':'#8B8B8B','$TOGGLE-COLOR$':'#38a6a6','$ARROW-COLOR$':'#ffffff'}

def makeNavbarCSS(d):
	CSSFile=open('./layout/navbar_'+d['type']+'.css')
	CSSString=CSSFile.read()
	del d['type']
	for (key,value) in d.items():
		navbarDict['$'+key.upper()+'$']=value
	for (key,value) in navbarDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

fadeDict={'$CLASS$':'fade','$COLOR$':'#008CBA','$FONT-COLOR$':'white','$FONT-SIZE$':'20px','$LEFT$':'0','$BOTTOM$':'0','$WIDTH$':'0','$HEIGHT$':'0','$HOVER-HEIGHT$':'none','$HOVER-WIDTH$':'none','$HOVER-LEFT$':'none','$HOVER-BOTTOM$':'none','$OPACITY$':'none','$HOVER-OPACITY$':'none'}
topDict={'$BOTTOM$':'100%','$WIDTH$':'100%','$HOVER-HEIGHT$':'100%','$HOVER-BOTTOM$':'0'}
bottomDict={'$WIDTH$':'100%','$HOVER-HEIGHT$':'100%'}
leftDict={'$HEIGHT$':'100%','$HOVER-WIDTH$':'100%'}
rightDict={'$LEFT$':'100%','$HEIGHT$':'100%','$HOVER-WIDTH$':'100%','$HOVER-LEFT$':'0'}
noneDict={'$OPACITY$':'0','$HOVER-OPACITY$':'1','$WIDTH$':'100%','$HEIGHT$':'100%'}
typeDict={'top':topDict,'bottom':bottomDict,'right':rightDict,'left':leftDict}

def makeFadeCSS(d):
	CSSFile=open('./layout/fade.css')
	CSSString=CSSFile.read()
	newfadeDict=copy.deepcopy(fadeDict)
	if(d['type']):
		newfadeDict.update(typeDict[d['type']])
	else:
		newfadeDict.update(noneDict)
	del d['type']
	for (key,value) in d.items():
		newfadeDict['$'+key.upper()+'$']=value
	for (key,value) in newfadeDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

cardDict={'$CLASS$':'.card','$COLOR$':'white','$FONT-COLOR$':'black','$FONT-SIZE$':'none','$PADDING-TOP$':'10px','$PADDING-LEFT$':'20px'}

def makeCardCSS(d):
	CSSFile=open('./layout/card.css')
	CSSString=CSSFile.read()
	newcardDict=copy.deepcopy(cardDict)
	for (key,value) in d.items():
		newcardDict['$'+key.upper()+'$']=value
	for (key,value) in newcardDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

def makeParallaxCSS(d):
	CSSFile=open('./layout/parallax.css')
	CSSString=CSSFile.read()
	CSSString=CSSString.replace('$CLASS$',d['class'])
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

footerDict={'$COLOR$':'#292c2f','$FONT-COLOR$';'#ffffff','$FONT-SIZE$':'18px','$MOTTO-FONT-COLOR$':'#8d9093','$MOTTO-FONT-SIZE$':'24px','$NAME-FONT-COLOR$':'#8f9296','$NAME-FONT-SIZE$':'14px'}

def makeFooterCSS(d):
	CSSFile=open('./layout/footer_'+d['type']+'.css')
	CSSString=CSSFile.read()
	del d['type']
	for (key,value) in d.items():
		footerDict['$'+key.upper()+'$']=value
	for (key,value) in footerDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

CSSDict={'card':makeCardCSS,'fade':makeFadeCSS,'navbar':makeNavbarCSS,'parallax':makeParallaxCSS}

def makeCSS(d):
	CSSDict[list(d.keys())[0]](d[list(d.keys())[0]])