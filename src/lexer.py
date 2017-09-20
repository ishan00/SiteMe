import ply.lex as lex

tokens=['KEYWORD','STYLE','REST','NEWLINE']

t_KEYWORD=r'(title|font-size|background-color):[0-9a-zA-Z ][a-zA-Z0-9 ]*'
t_STYLE=r'(image|link|list)?\{[^\(\)\{\}]*?\}\([^\(\)\{\}]*?\)'
t_REST=r'(?!(title|font-size|background-color):[0-9a-zA-Z][a-zA-Z0-9]*)(?:(?!(image|link|list)?\{[^\(\)\{\}]*?\}\([^\(\)\{\}]*?\)).)+'
t_NEWLINE=r'\n\r|\r\n|\r|\n'

lexer=lex.lex()

# a=open("SiteMe/pages/index.txt")
# b=a.read()
# lexer.input(b.strip())
# #print(b.strip())
# print([t for t in lexer])
