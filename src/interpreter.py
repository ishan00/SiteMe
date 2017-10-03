import re
#from lexer import keywords
from sys import argv

script , pagefile , configfile = argv

short_syntax = {'r' : "'align':'right'" , 'l' : "'align':'left'"}


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
def filler(d,path,replace):
	if(len(path) == 1):
		d[path[0]] = replace
		return d
	else:
		d[path[0]] = filler(d[path[0]] , path[1:],replace)
		return d
'''
This function converts dictionaries to html codes.
Note: It is assumed that styles provided are valid
'''
standAlone=['href', 'src', 'class', 'id']
Tags={'img':False,'br':False,'hr':False,'header':True,'footer':True,'a':True,'table':True,'ul':True,'ol':True,'h1':True,'h2':True,'h3':True,'h4':True,'h5':True,'h6':True,'b':True,'li':True,'ol':True,'i':True,'script':True,'div':True,'span':True,'nav':True,'button':True}
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
				rs="\n<"+Tag;
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
						for i in range(0,len(d['content'])):
							rs=rs+makeHTML(d['content'][i+1])
					else:
						rs=rs+d['content']
					rs=rs+"</"+Tag+">\n"
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

def makePage():
	config = open(configfile)
	page = open(pagefile)
	l_c = config.readlines()
	l_p = page.readlines()
	navbar = ""
	footer = ""
	content = ""
	title = ""
	infile_css = ""
	for i in l_c:
		temp = parseAbstractElement(i)
		if(temp[0] == 'navbar'):
			navbar = temp
		elif(temp[0] == 'footer'):
			footer = temp
	for i in l_p:
		if(i[0:3] == '###'):
			if(i.count('title') == 1):
				title = i[i.find(':') + 1:]
			elif(i[3:].split(':')[0].strip() in keywords):
				infile_css = infile_css + i[3:].strip('\n')+';\n'
			else:
				content=content+i
		else:
			content = content + i
	print ("<html>")
	print ("<head>")
	print ("<title>" + title + "</title>")
	print ('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">')
	print ("<link rel=\"stylesheet\" href=\"./css/style.css\">")
	print ("<style>")
	print ("body {")
	print (infile_css + "}")
	print ('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>')
	print ('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>')
	print ("</style>")
	print ("</head>")
	print ("<body>")
	#print (makeNavbar(navbar[1],'layout/navbar.html'))
	print (content)
	print (makeFooter(footer[1], 'layout/footer.html'))
	print ("</body>")
	print ("</html>")

line_from_config = 'navbar(type1){Home:{a:alpha,b:beta},About:about.com,Contact:contact.org,Blog:blog.com}'
print (parseAbstractElement(line_from_config))
