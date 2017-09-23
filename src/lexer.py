import ply.lex as lex

tokens=['KEYWORD','PRE','STYLE','REST','NEWLINE']
keywords=['title','font-size','background-color']
styles=['image','link','list','piechart']

def t_error(t):
	return
t_KEYWORD=r'[#]*('+'|'.join(keywords)+'):[0-9a-zA-Z ][a-zA-Z0-9() ,]*'
t_STYLE=r'('+'|'.join(styles)+')?\([^\(\)\{\}]*?\)\{[^\(\)\{\}]*?\}'
t_PRE=r'\(Pre\)\{\{.*\}\}'
#t_REST=r'(?:(?![#]*('+'|'.join(keywords)+'):[0-9a-zA-Z ][a-zA-Z0-9 (),]*).)+(?:(?!('+'|'.join(styles)+')?\([^\(\)\{\}]*?\)\{[^\(\)\{\}]*?\}).)+(?:(?!\(Pre\)\{\{.*\}\}).)+'
t_REST=r'.'
t_NEWLINE=r'\n\r|\r\n|\r|\n'

# precedence=(
# 	('left', 'PRE'),
# 	('left', 'STYLE', 'KEYWORD', 'NEWLINE'),
# 	('left', 'REST'),
# 	)

lexer=lex.lex()

a=open("../pages/index.txt")
b=a.read()
lexer.input(b.strip())
#print(b.strip())
print([t for t in lexer])
