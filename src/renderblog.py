from __future__ import print_function
from sys import argv
script, blogfile, directoryFile = argv
import sys
import os
import copy

directory = os.fsencode(directoryFile)
def eprint(*args, **kwargs):
	print (*args, file=sys.stderr, **kwargs)
tags = {}
archive = {}

blog_page = '''#nonavbar
#nofooter
grid(2,8,2){}{
	$FULLCONTENT$	
}
{}
'''
post_content = '''
(center,h1){$TITLE$}
(h3,color:#eeeeee,center){$AUTHOR$}
(color:#eeeeee){$DATE$}
$CONTENT$
-------'''

CONTENT = ''

file_list = [os.fsdecode(post) for post in os.listdir(directory)]
file_list.sort()
#eprint(file_list)
for post in file_list:
	f = open(os.fsdecode(directory) + post)
	f = f.readlines()
	new_post = copy.deepcopy(post_content)
	body_content = ''
	liquid_tags = True
	for line in f:
		#eprint(line)
		if liquid_tags:
			if(line.find('title:') != -1):
				new_post = new_post.replace('$TITLE$',line.split(':',1)[1].strip())
			elif (line.find('author:') != -1):
				new_post = new_post.replace('$AUTHOR$',line.split(':',1)[1].strip())
			elif (line.find('date:') != -1):
				new_post = new_post.replace('$DATE$',line.split(':',1)[1].strip())
			elif (line.find('-----') != -1):
				liquid_tags = False
		else:
			body_content = body_content + line

	new_post = new_post.replace('$CONTENT$',body_content)
	#eprint(new_post)
	CONTENT = CONTENT  + new_post + '||'
blog_page = blog_page.replace('$FULLCONTENT$',CONTENT)

final_file = open(blogfile, 'r+')
final_file.write(blog_page)
#eprint(blog_page)
'''
This file should take as input a blog post, ie posts/*.siteme and convert it into HTML and paste it at pages/blog.siteme
'''

