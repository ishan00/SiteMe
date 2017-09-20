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
	print ("</head>")

if __name__ == '__main__':
	main()