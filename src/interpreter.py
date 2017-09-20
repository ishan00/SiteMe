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

# This function doesn't have much use. There should be a generic make_dict which does (a:b , ) -> {a:b , }
def makeNavbar(dict,filename):
	keystr="#####"
	valuestr="$$$$$"
	file=open(filename)
	line=file.readline().strip();
	navbar=line[:]
	line=file.readline().strip();
	while(line):
		if(line.find(keystr)):
			line=line.replace(keystr,dict[0][0])
			line=line.replace(valuestr,dict[0][1])
			navbar=navbar+""""\n"""+line
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
		return navbar

def make_tuples(s):
	'''
	Input - Output
	link{abcd.com}(Home),link{facebook.com}(About) - [ ("Home","abcd.com") , ("About","facebook.com") ]
	'''
	s_list = s.split(',')
	s_tuples = []
	for elem in s_list:
		split = lexString(elem)
		s_tuples.append((split[1],split[2]))
	return s_tuples

def parseAbstractElement(s):
	'''
	Input - Output
	navbar{link{abcd.com}(Home),link{facebook.com}(About)}(type1) - [Type , dict_{} , dict_()]
	'''
	matchObj = re.match( r'([^{]*){(.*)}\((.*)\)' , s)
	if matchObj:
		keyword = matchObj.group(1)
		content = matchObj.group(2)
		style =  matchObj.group(3)
		#print ("matchObj.group() : ", matchObj.group())
		#print ("matchObj.group(1) : ", matchObj.group(1))
		#print ("matchObj.group(2) : ", matchObj.group(2))
		#print ("matchObj.group(2) : ", matchObj.group(3))
		return [keyword , make_dict(content) , style]
	else:
		print ("No match!!")
		return []

def makePage():
	config = open('../config.txt')
	page = open('../tmp/index.temp')
	print ("<head>")
	print ("<title>" + title + "</title>")
	print ("<style>")
	print ("body {")
	#
	print ("}")
	print ("</style>")
	print ("</head>")
	print ("<body>")
	print (makeNavbar())

if __name__ == '__main__':
	main()
