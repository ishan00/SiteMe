import re

def dict(a):
	element = a.split(',')
	for

def titleLine(str):
	return (str.find('title') != -1)
def styleLine(str):
	return (str.find('font') != -1)

config_file=open('config.txt')
lines = config_file.readlines()
l1 = [line.strip('\n') for line in lines]

page_file = open('./pages/index.txt')
l2 = [line.strip('\n') for line in page_file.readlines()]

#print(l1)
#print(l2)

print ("""
<html>
<head>
""")

for temp_line in l2:
	if(titleLine(temp_line)):
		print ("<title>" + temp_line[temp_line.find(':')+1:] + "</title>")
	elif(styleLine(temp_line)):
		print ("<style>")
		print ("body{")
		print ("font-size:" + temp_line[temp_line.find(':')+1:])
		print ("}")
		print ("</style>")

print ("""
</head>
<body>
""")

for temp_line in l1:
	if(temp_line.find('navbar') != -1):
		navbar = dict(temp_line[6:])


print ("""
</body>
</html>
""")
