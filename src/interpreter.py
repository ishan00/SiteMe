import re
#from lexer import keywords


'''
Boolean function which returns true if the keyword given goes inside style=""

TODO Add an exhaustive list of keywords
'''
def isContained(s):
	keywords = {'id':False , 'href':False , 'class':False , 'width':True , 'height':True , 'background-color':True , 'font-size':True}
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
			standalone_str = standalone_str + ('%s="%s" ')%(keyword,d[keyword])
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

{a:{href:url} , content:Text}

<a href=url>Text</a>

{li:{class:"active"} , content:<a href=url>Text</a>}

<li class="active"><a href=url>Text</a></li>

{ul:{} , content:<li class="active"><a href=url>Text</a></li>}

<ul>
	<li class="active"><a href=url>Text</a></li>
</ul>

{div:{class=navbar} content:<ul>\n<li class="active"><a href=url>Text</a></li>\n</ul>}
<div class="navbar">
	<ul>
		<li class="active"><a href=url>Text</a></li>
	</ul>
</div>

There we have our navbar complete using this function recursively.
'''
def ContainerElement(d,newline):
	container_name = list(d.keys())
	container_name.remove('content');
	result = ""
	if (newline):
		result = '\n'.join((('<%s %s>'%(container_name[0] , attributeString(d[container_name[0]]))) , d['content'] ,('</%s>'%container_name[0])))
	else:
		result = ' '.join((('<%s %s>'%(container_name[0] , attributeString(d[container_name[0]]))) , d['content'] ,('</%s>'%container_name[0])))
	return result

def lexString(s): 
	'''
	Input - Output
	"{content}(style)" - [ content, style ]
	"keyword{content}(style)" - [ content , style , keyword ]
	'''
	matchObj = re.match( r'(.*){(.*)}\((.*)\)' , s)
	if matchObj:
		keyword = matchObj.group(1)
		content = matchObj.group(2)
		style =  matchObj.group(3)
		return [keyword , style , content]
	else:
		print ("No match!!")
		return []

def make_tuples(s):
	'''
	Input - Output
	Home:a.com,About:facebook.com - [ ("Home","abcd.com") , ("About","facebook.com") ]
	'''
	s_list = s.split(',')
	s_tuples = []
	for elem in s_list:
		split = elem.split(":")
		s_tuples.append((split[0],split[1]))
	return s_tuples

def makePage():
	config = open('config.siteme')
	page = open('tmp/index.tmp')
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
	#makeCSS("./layout/navbar.css","navbar")
	makeCSS("./layout/footer.css","footer")