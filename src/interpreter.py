import re

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

def makeNavbar(dict,filename):
	keystr="#####"
	valuestr="$$$$$"
	file=open(filename)
	line=file.readline().strip();
	navbar='''<div class="navbar">\n'''+line[:]
	line=file.readline().strip();
	while(line):
		if(line.find(keystr)):
			line=line.replace(keystr,dict[0][0])
			line=line.replace(valuestr,dict[0][1])
			navbar=navbar+"\n"+line
			line=file.readline().strip()
			break
		else:
			navbar=navbar+"\n"+line
			line=file.readline().strip()
	for (key,value) in dict[1:]:
		cline=line[:]
		cline=cline.replace(keystr,key)
		cline=cline.replace(valuestr,value)
		navbar=navbar+"\n"+cline
	line=file.readline().strip()
	while(line):
		navbar=navbar+"\n"+line
		line=file.readline().strip()
	navbar=navbar+"\n</div>"
	return navbar

def makeCSS(filename):
	file=open(filename)
	line=file.readline()
	wfile=open("./site/css/style.css",'a')
	while(line):
		if(line.count('{')==1):
			line=".navbar "+line
			wfile.write(line)
			line=file.readline()
		else:
			wfile.write(line)
			line=file.readline()



# There should be a generic make_dict which does (a:b , ) -> {a:b , }

def make_tuples(s):
	'''
	Input - Output
	Home:a.com,About:facebook.com - [ ("Home","abcd.com") , ("About","facebook.com") ]
	'''
	s_list = s.split(',')
	s_tuples = []
	for elem in s_list:
		split = elem.split[:]
		s_tuples.append((split[0],split[1]))
	return s_tuples

def parseAbstractElement(s):
	'''
	Input - Output
	navbar(type1){Home:a.com,About:b.com} - [Type , dict_{} , dict_()]
	'''
	matchObj = re.match( r'(.*)\((.*)\){(.*)}' , s)
	if matchObj:
		keyword = matchObj.group(1)
		style = matchObj.group(2)
		content =  matchObj.group(3)
		#print ("matchObj.group() : ", matchObj.group())
		#print ("matchObj.group(1) : ", matchObj.group(1))
		#print ("matchObj.group(2) : ", matchObj.group(2))
		#print ("matchObj.group(2) : ", matchObj.group(3))
		return [keyword , make_tuples(content) , style]
	else:
		print ("No match!!")
		return []

def makePage():
	config = open('config.txt')
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
		if(i[0] == '#'):
			if(i.count('title') == 1):
				title = i[i.find(':') + 1:]
			else:
				infile_css = infile_css + i[1:]
		else:
			content = content + i
	print ("<html>")
	print ("<head>")
	print ("<title>" + title + "</title>")
	print ("<link rel=\"stylesheet\" href=\"./css/style.css\">")
	print ("<style>")
	print ("body {")
	print (infile_css + "}")
	print ("</style>")
	print ("</head>")
	print ("<body>")
	print (makeNavbar(navbar[1],'layout/navbar.html'))
	print (content)
	print ("</body>")
	print ("</html>")
	makeCSS("./layout/navbar.css")

makePage()
#navbar = parseAbstractElement("navbar{link{a.com}(Home),link{b.com}(About),link{c.com}(Contact)}(type1)")
#print (makeNavbar(navbar[1],'layout/navbar.html'))