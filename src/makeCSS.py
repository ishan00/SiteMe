'''
	This file creates the css file corresponding to each file in pages
	The files are named like <page_name>.siteme -> <page_name>.css and placed inside the css folder of site

	Input (Some features will be implemented later yet I have written them in input for consistency)
	{
		navbar : { type : type1 , class : class_name }
		header : { type : type2 , class : class_name }
		footer : { type : type3 , class : class_name }
		table  : { type : type4 , class : class_name , style : {border: val , background-color : color ,  alternate : color , width : 100px ,padding : val} }
		slideshow : { type : carousel , class : class_name , content : {img1 : path , img2: path , ...} }
		grid : { type : type1 , class : class_name , size : (a,b) , content : { {img, title , button , description} * (ab times) }  }
		cover : { type : type2 , class : class_name , content : {img : path , title :  , description : short_description } } 
	}
'''

def 