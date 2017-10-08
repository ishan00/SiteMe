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
navbarDict={'$CLASS$':'.navbar','$COLOR$':'#f96e5b','$FONT-COLOR$':'#ffffff','$FONT-SIZE$':'14px','$HOVER-COLOR$':'#ffffff','$HOVER-FONT-COLOR$':'#333333'.'$DROPDOWN-COLOR$':'none','$DROPDOWN-FONT-COLOR$':'#8B8B8B','$TOGGLE-COLOR$':'#38a6a6','$ARROW-COLOR$':'#ffffff'}

def makeNavbarCSS(d):
	CSSFile=open('../layout/navbar_'+d['type']+'.css')
	CSSString=CSSFile.read()
	del d['type']
	for (key,value) in d.items():
		navbarDict['$'+key.upper()+'$']=value
	for (key,value) in navbarDict.items():
		CSSString=CSSString.replace(key,value)
	styleFile=open('../site/css/style.css','a')
	styleFile.write(CSSString)
	styleFile.close()

makeNavbarCSS({'type':'orange','class':'.oho','font-color':'blue','color':'red'})

