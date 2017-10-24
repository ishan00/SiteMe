import ply.lex as lex
from sys import argv

#script , filename = argv

tokens=['KEYWORD','PRE', 'CODE','STYLE','REST','NEWLINE','HRULE','GRID']
keywords=['title','font-size','background-color']
styles=['image','link','list','piechart','table','slideshow','parallax','fade','card','button', 'accordion', 'timeline',
'chatbox','checkbox','alert','wallpaper', 'skillbar','tooltip','textfield','passwordfield','select','submit','form','block']

def t_error(t):
	return
t_KEYWORD=r'([#]*('+'|'.join(keywords)+'):[0-9a-zA-Z #][a-zA-Z0-9() ,#]*)|(\#[a-zA-Z]+)'
t_STYLE=r'('+'|'.join(styles)+')?\([^\(\)\{\}]*?\)\{[^\(\)\{\}]*?\}'
t_PRE=r'\((latex|pre)\)\{\{[\s\S]*?\}\}'
t_CODE=r'\(code\)\{\{[\s\S]*?\}\}'
#t_GRID=r'grid\([\s\S]*?\)(\{[^\{\}]*[\n ]*([^\{\}]*[\n ]*\{[^\{\}]*[\n ]*\}[^\{\}]*[\n ]*)*[^\{\}]*[\n ]*\})+'
t_GRID=r'grid\([\s\S]*?\)(\{[^\{\}]*?\}[\n ]*)*'
t_HRULE=r'-{5,}'
t_REST=r'(?:(?!(([#]*('+'|'.join(keywords)+'):[0-9a-zA-Z #][a-zA-Z0-9() ,#]*)|(\#[a-zA-Z]+)|('+'|'.join(styles)+')?\([^\(\)\{\}]*?\)\{[^\(\)\{\}]*?\}|grid\([\s\S]*?\)(\{[^\{\}]*?\}[\n ]*)*|\((latex|pre)\)\{\{[\s\S]*?\}\}|\(code\)\{\{[\s\S]*?\}\}|-{5,})).)+'
t_NEWLINE=r'\n\r|\r\n|\r|\n'

# precedence=(
# 	('left', 'REST'),
# 	('left', 'KEYWORD', 'NEWLINE'),
# 	('left', 'STYLE'),
# 	('left', 'PRE'),
# 	)

lexer=lex.lex()

#a=open("./pages/index.sm")
#b=a.read()
#lexer.input(b.strip())
#print(b.strip())
#print([t for t in lexer])
