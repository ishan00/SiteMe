import copy
from itertools import cycle
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
tooltipDict={'$COLOR':'#555','$FONT-COLOR$':'#fff','$CLASS$':'.tooltip'}

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

footerDict={'$CLASS$':'.footer','$COLOR$':'#292c2f','$FONT-COLOR$':'#ffffff','$FONT-SIZE$':'18px','$MOTTO-FONT-COLOR$':'#8d9093','$MOTTO-FONT-SIZE$':'24px','$NAME-FONT-COLOR$':'#8f9296','$NAME-FONT-SIZE$':'14px','$SIZE':'60px'}

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

buttonDict={'$CLASS$':'#button','$COLOR$':'#4CAF50','$BORDER-COLOR$':'none','$FONT-COLOR$':'white','$PADDING-TOP$':'15px','$PADDING-LEFT$':'32px','$FONT-SIZE$':'16px','$CURSOR$':'pointer','$ROUNDED$':'none','$OPACITY$':'none','$SHADOW$':'none','$HOVER-COLOR$':'none','$HOVER-FONT-COLOR$':'none','$HOVER-SHADOW$':'none','$DROPDOWN-COLOR$':'#f9f9f9','$DROPDOWN-FONT-COLOR$':'black','$DROPDOWN-FONT-SIZE$':'none','$DROPDOWN-WIDTH$':'160px','$DROPDOWN-HOVER-COLOR$':'#f1f1f1','$DROPDOWN-HOVER-FONT-COLOR$':'black'}

def makeButtonCSS(d):
	CSSFile=open('./layout/button.css')
	CSSString=CSSFile.read()
	newbuttonDict=copy.deepcopy(buttonDict)
	for (key,value) in d.items():
		newbuttonDict['$'+key.upper()+'$']=value
	for (key,value) in newbuttonDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

def makeHoverButtonCSS(d):
	CSSFile=open('./layout/hover-dropdown.css')
	CSSString=CSSFile.read()
	newbuttonDict=copy.deepcopy(buttonDict)
	for (key,value) in d.items():
		newbuttonDict['$'+key.upper()+'$']=value
	for (key,value) in newbuttonDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

def makeClickButtonCSS(d):
	CSSFile=open('./layout/click-dropdown.css')
	CSSString=CSSFile.read()
	newbuttonDict=copy.deepcopy(buttonDict)
	for (key,value) in d.items():
		newbuttonDict['$'+key.upper()+'$']=value
	for (key,value) in newbuttonDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

def makeAccordionCSS(d):
	CSSFile = open('./layout/accordion.css')
	CSSString = CSSFile.read()
	styleFile = open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

def makeCheckBoxCSS(d):
	CSSFile = open('./layout/checkbox.css')
	CSSString = CSSFile.read()
	CSSString = CSSString.replace('$CLASS$',d['class'])
	styleFile = open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

def makeImageFlipCSS(d):
	CSSFile = open('./layout/flip.css')
	CSSString = CSSFile.read()
	CSSString = CSSString.replace('$CLASS$',d['class'])
	styleFile = open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

def makeImageShakeCSS(d):
	CSSFile = open('./layout/shake.css')
	CSSString = CSSFile.read()
	CSSString = CSSString.replace('$CLASS$',d['class'])
	styleFile = open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

alertDict = {'$CLASS$':'', '$COLOR$':'red' , '$TEXT-COLOR':'white'}

def makeAlertCSS(d):
	CSSFile = open('./layout/alert.css')
	CSSString = CSSFile.read()
	newalertDict =copy.deepcopy(alertDict)
	for (key,value) in d.items():
		newalertDict['$'+key.upper()+'$']=value
	for (key,value) in newalertDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

wallpaper_type1Dict = {'$CLASS$':'' , '$COLOR$':'#1abc9c' , '$TEXT-COLOR$':'#ffffff'}

def makeWallpaperCSS(d):
	CSSFile = open('./layout/wallpaper_' + d['type'] + '.css')
	CSSString = CSSFile.read()
	newWallpaperDict =copy.deepcopy(wallpaper_type1Dict)
	for (key,value) in d.items():
		newWallpaperDict['$'+key.upper()+'$']=value
	for (key,value) in newWallpaperDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

def makeTimelineCSS(d):
	CSSFile = open('./layout/timeline.css')
	CSSString = CSSFile.read()
	CSSString = CSSString.replace('$CLASS$',d['class'])
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

COLORS = ['#4CAF50' , '#2196F3','#e10d0d' , '#fed044' , '#00c992' , '#7e1dfb']

gen_color = cycle(COLORS)

blockDict = {'$SHADOW$':'4px' , '$PADDING-TOP$':'20px', '$PADDING-RIGHT$':'16px', '$WIDTH$':'100%' , '$COLOR$':'white' , '$MARGIN-TOP$':'12px' , '$MARGIN-RIGHT$':'4px' , '$MARGIN-BOTTOM$':'12px', '$MARGIN-LEFT$':'4px'}

def makeBlockCSS(d):
	CSSFile = open('./layout/block.css')
	CSSString = CSSFile.read()
	newBlockDict =copy.deepcopy(blockDict)
	for (key,value) in d.items():
		newBlockDict['$'+key.upper()+'$']=value
	for (key,value) in newBlockDict.items():
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

def makeTooltipCSS(d):
	CSSFile=open('./layout/tooltip.css')
	CSSString=CSSFile.read()
	newtooltipDict=copy.deepcopy(tooltipDict)
	for (key,value) in d.items():
		newtooltipDict['$'+key.upper()+'$']=value
	for (key,value) in newtooltipDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

def makeChatboxCSS(d):
	CSSFile = open('./layout/chatbox.css')
	CSSString = CSSFile.read()
	CSSString = CSSString.replace('$CLASS$',d['class'])
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

textfieldDict={'$CLASS$':'.textfield','$FONT-SIZE$':'16px','$WIDTH$':'100%','$HEIGHT$':'none'}

def makeTextfieldCSS(d):
	CSSFile = open('./layout/formfield.css')
	CSSString = CSSFile.read()
	newtextfieldDict=copy.deepcopy(textfieldDict)
	for (key,value) in d.items():
		newtextfieldDict['$'+key.upper()+'$']=value
	for (key,value) in newtextfieldDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

passwordfieldDict={'$CLASS$':'.passwordfield','$FONT-SIZE$':'16px','$WIDTH$':'100%','$HEIGHT$':'none'}

def makePasswordfieldCSS(d):
	CSSFile = open('./layout/formfield.css')
	CSSString = CSSFile.read()
	newpasswordfieldDict=copy.deepcopy(passwordfieldDict)
	for (key,value) in d.items():
		newpasswordfieldDict['$'+key.upper()+'$']=value
	for (key,value) in newpasswordfieldDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()	

selectDict={'$CLASS$':'.select','$FONT-SIZE$':'16px','$WIDTH$':'100%','$HEIGHT$':'none'}

def makeSelectCSS(d):
	CSSFile = open('./layout/formfield.css')
	CSSString = CSSFile.read()
	newselectDict=copy.deepcopy(selectDict)
	for (key,value) in d.items():
		newselectDict['$'+key.upper()+'$']=value
	for (key,value) in newselectDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

submitDict={'$CLASS$':'.submit','$COLOR$':'#4CAF50','$BORDER-COLOR$':'none','$FONT-COLOR$':'white','$PADDING-TOP$':'12px','$PADDING-LEFT$':'20px','$FONT-SIZE$':'16px','$CURSOR$':'pointer','$ROUNDED$':'4px','$OPACITY$':'none','$SHADOW$':'none','$HOVER-COLOR$':'#45a049','$HOVER-FONT-COLOR$':'none'}

def makeSubmitCSS(d):
	CSSFile = open('./layout/submit.css')
	CSSString = CSSFile.read()
	newsubmitDict=copy.deepcopy(submitDict)
	for (key,value) in d.items():
		newsubmitDict['$'+key.upper()+'$']=value
	for (key,value) in newsubmitDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('./site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

CSSDict={
	'card':makeCardCSS,
	'fade':makeFadeCSS,
	'navbar':makeNavbarCSS,
	'parallax':makeParallaxCSS,
	'footer':makeFooterCSS,
	'button':makeButtonCSS,
	'hover-button':makeHoverButtonCSS,
	'click-button':makeClickButtonCSS,
	'accordion':makeAccordionCSS,
	'checkbox':makeCheckBoxCSS,
	'flip':makeImageFlipCSS,
	'shake':makeImageShakeCSS,
	'alert':makeAlertCSS,
	'wallpaper':makeWallpaperCSS,
	'timeline':makeTimelineCSS,
	'skillbar':makeSkillbarCSS,
	'tooltip':makeTooltipCSS,
	'chatbox':makeChatboxCSS,
	'textfield':makeTextfieldCSS,
	'passwordfield':makePasswordfieldCSS,
	'select':makeSelectCSS,
	'submit':makeSubmitCSS,
	'block':makeBlockCSS
}


def makeCSS(d):
	CSSDict[list(d.keys())[0]](d[list(d.keys())[0]])
