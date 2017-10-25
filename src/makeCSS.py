import copy
from itertools import cycle

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

navbarDict={'$CLASS$':'.navbar','$COLOR$':'#f96e5b','$FONT-COLOR$':'#ffffff','$FONT-SIZE$':'14px','$HOVER-COLOR$':'#ffffff','$HOVER-FONT-COLOR$':'#333333','$DROPDOWN-COLOR$':'none','$DROPDOWN-FONT-COLOR$':'#8B8B8B','$TOGGLE-COLOR$':'#38a6a6','$ARROW-COLOR$':'#ffffff'}
footerDict={'$CLASS$':'.footer','$COLOR$':'#292c2f','$FONT-COLOR$':'#ffffff','$FONT-SIZE$':'18px','$MOTTO-FONT-COLOR$':'#8d9093','$MOTTO-FONT-SIZE$':'24px','$NAME-FONT-COLOR$':'#8f9296','$NAME-FONT-SIZE$':'14px','$SIZE':'60px'}
wallpaper_type1Dict = {'$CLASS$':'' , '$COLOR$':'#1abc9c' , '$TEXT-COLOR$':'#ffffff'}

def makeTypeGenCSS(d,f,x):
	CSSFile = open(f + d['type'] + '.css')
	CSSString = CSSFile.read()
	newDict =copy.deepcopy(x)
	for (key,value) in d.items():
		newDict['$'+key.upper()+'$']=value
	for (key,value) in newDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

def makeSkillbarCSS(d):
	CSSFile = open('./layout/skillbar.css')
	CSSString = CSSFile.read()
	CLASSNAME = d['class']
	CSSString = CSSString.replace('$CLASS$', CLASSNAME)
	del d['class']
	for u,v in d.items():
		CSSString = CSSString + '\n' + CLASSNAME + ' ' + u + ' {width:' + v + '; background-color:' + next(gen_color) + ';}\n'
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

cardDict={'$CLASS$':'.card','$COLOR$':'white','$FONT-COLOR$':'black','$FONT-SIZE$':'none','$PADDING-TOP$':'10px','$PADDING-LEFT$':'20px'}
parallaxDict={'$CLASS$':'.parallax'}
accordionDict={}
buttonDict={'$CLASS$':'#button','$COLOR$':'#4CAF50','$BORDER-COLOR$':'none','$FONT-COLOR$':'white','$PADDING-TOP$':'15px','$PADDING-LEFT$':'32px','$FONT-SIZE$':'16px','$CURSOR$':'pointer','$ROUNDED$':'none','$OPACITY$':'none','$SHADOW$':'none','$HOVER-COLOR$':'none','$HOVER-FONT-COLOR$':'none','$HOVER-SHADOW$':'none','$DROPDOWN-COLOR$':'#f9f9f9','$DROPDOWN-FONT-COLOR$':'black','$DROPDOWN-FONT-SIZE$':'none','$DROPDOWN-WIDTH$':'160px','$DROPDOWN-HOVER-COLOR$':'#f1f1f1','$DROPDOWN-HOVER-FONT-COLOR$':'black'}
checkboxDict={'$CLASS$':'.chatbox'}
flipDict={'$CLASS$':'.chatbox'}
shakeDict={'$CLASS$':'.chatbox'}
alertDict = {'$CLASS$':'', '$COLOR$':'red' , '$TEXT-COLOR':'white'}
timelineDict={'$CLASS$':'.chatbox'}
tooltipDict={'$COLOR':'#555','$FONT-COLOR$':'#fff','$CLASS$':'.tooltip'}
chatboxDict={'$CLASS$':'.chatbox'}
textfieldDict={'$CLASS$':'.textfield','$FONT-SIZE$':'16px','$WIDTH$':'100%','$HEIGHT$':'none'}
passwordfieldDict={'$CLASS$':'.passwordfield','$FONT-SIZE$':'16px','$WIDTH$':'100%','$HEIGHT$':'none'}
selectDict={'$CLASS$':'.select','$FONT-SIZE$':'16px','$WIDTH$':'100%','$HEIGHT$':'none'}
submitDict={'$CLASS$':'.submit','$COLOR$':'#4CAF50','$BORDER-COLOR$':'none','$FONT-COLOR$':'white','$PADDING-TOP$':'12px','$PADDING-LEFT$':'20px','$FONT-SIZE$':'16px','$CURSOR$':'pointer','$ROUNDED$':'4px','$OPACITY$':'none','$SHADOW$':'none','$HOVER-COLOR$':'#45a049','$HOVER-FONT-COLOR$':'none'}
COLORS = ['#4CAF50' , '#2196F3','#e10d0d' , '#fed044' , '#00c992' , '#7e1dfb']
gen_color = cycle(COLORS)
blockDict = {'$SHADOW$':'4px' , '$PADDING-TOP$':'20px', '$PADDING-RIGHT$':'16px', '$WIDTH$':'100%' , '$COLOR$':'white' , '$MARGIN-TOP$':'12px' , '$MARGIN-RIGHT$':'4px' , '$MARGIN-BOTTOM$':'12px', '$MARGIN-LEFT$':'4px'}

def makeGenCSS(d,f,x):
	CSSFile = open(f)
	CSSString = CSSFile.read()
	newDict=copy.deepcopy(x)
	for (key,value) in d.items():
		newDict['$'+key.upper()+'$']=value
	for (key,value) in newDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

genCSSDict={
	'card':['./layout/card.css',cardDict],
	'parallax':['./layout/parallax.css',parallaxDict],
	'accordion':['./layout/accordion.css',accordionDict],
	'button':['./layout/button.css',buttonDict],
	'hover-button':['./layout/hover-dropdown.css',buttonDict],
	'click-button':['./layout/click-dropdown.css',buttonDict],
	'checkbox':['./layout/checkbox.css',checkboxDict],
	'flip':['./layout/flip.css',flipDict],
	'shake':['./layout/shake.css',shakeDict],
	'alert':['./layout/alert.css',alertDict],
	'timeline':['./layout/timeline.css',timelineDict],
	'tooltip':['./layout/tooltip.css',tooltipDict],
	'chatbox':['./layout/chatbox.css',chatboxDict],
	'textfield':['./layout/formfield.css',textfieldDict],
	'passwordfield':['./layout/formfield.css',passwordfieldDict],
	'select':['./layout/formfield.css',selectDict],
	'submit':['./layout/submit.css',submitDict],
	'block':['./layout/block.css',blockDict]
}

typeGenCSSDict={
	'navbar':['./layout/navbar_',navbarDict],
	'footer':['./layout/footer_',footerDict],
	'wallpaper':['./layout/wallpaper_',wallpaper_type1Dict]
}

CSSDict={
	'fade':makeFadeCSS,
	'skillbar':makeSkillbarCSS
}

def makeCSS(d):
	if(list(d.keys())[0] in genCSSDict.keys()):
		makeGenCSS(d[list(d.keys())[0]],genCSSDict[list(d.keys())[0]][0],genCSSDict[list(d.keys())[0]][1])
	elif(list(d.keys())[0] in typeGenCSSDict.keys()):
		makeTypeGenCSS(d[list(d.keys())[0]],typeGenCSSDict[list(d.keys())[0]][0],typeGenCSSDict[list(d.keys())[0]][1])
	else:
		CSSDict[list(d.keys())[0]](d[list(d.keys())[0]])
