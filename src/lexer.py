import ply.lex as lex

tokens=['KEYWORD','STYLE','REST','NEWLINE']
keywords=['title','font-size','background-color']
styles=['image','link','list','piechart']

def t_error(t):
	return
t_KEYWORD=r'[#]*('+'|'.join(keywords)+'):[0-9a-zA-Z ][a-zA-Z0-9() ,]*'
t_STYLE=r'('+'|'.join(styles)+')?\([^\(\)\{\}]*?\)\{[^\(\)\{\}]*?\}'
t_REST=r'(?![#]*('+'|'.join(keywords)+'):[0-9a-zA-Z ][a-zA-Z0-9() ,]*)(?:(?!('+'|'.join(styles)+')?\([^\(\)\{\}]*?\)\{[^\(\)\{\}]*?\}).)+'
t_NEWLINE=r'\n\r|\r\n|\r|\n'

lexer=lex.lex()

# a=open("../pages/index.txt")
# b=a.read()
# lexer.input(b.strip())
# #print(b.strip())
# print([t for t in lexer])
