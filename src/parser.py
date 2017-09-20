import ply.yacc as yacc
from sys import argv
import re
import lexer
tokens=lexer.tokens

def styleConv(s):
    stype=s.split('(')[0]
    sstyle=s.split('(')[1].split(')')[0]
    scontent=s.split('(')[1].split(')')[1].strip('{}')
    sstyle=sstyle.split(',')
    sstyle=';'.join(sstyle)
    if(stype=="image"):
        if scontent:
            rs="<img src=\"../img/"+scontent.strip()+"\" style=\""+sstyle.strip()+";\">"
    elif(stype=="link"):
        if scontent:
            if sstyle:
                rs="<a href=\""+scontent.strip()+"\">"+sstyle.strip()+"</a>"
            else:
                rs="<a href=\""+scontent.strip()+"\">"+scontent.strip()+"</a>"
    elif(stype=="list"):
        if scontent:
            if sstyle:
                rs="<"+sstyle.strip()+"l>"+''.join(["<li>"+x+"</li>\n" for x in [y.strip() for y in scontent.split('*')[1:]]])+"</"+sstyle.strip()+"l>"
    else:
        if scontent:
            if(sstyle=="bold"):
                rs="<span><b>"+scontent+"</b></span>"
            elif(sstyle[0]=='h'):
                rs="<span><"+sstyle.strip()+">"+scontent+"</"+sstyle.strip()+"></span>"
            else:
                rs="<span>"+scontent+"</span>"
    return rs

# def mainMaker(head,body):
#     rs="<html>\n<head>\n"+head+"\n</head>\n"+"<body>\n"+body+"\n</body>\n</html>"
#     return rs

def p_main(p):
    'main : head content'
    p[0]=p[1]+p[2]

def p_head(p):
    '''head : head keyword
            | head NEWLINE
            |
    '''
    if(len(p)==3):
        p[0]=p[1]+p[2]
    else:
        p[0]=''

def p_content(p):
    '''content : content style
               | content REST
               | content newline
               | 
    '''
    if(len(p)==3):
        p[0]=p[1]+p[2]
    else:
        p[0]=''

def p_style(p):
    'style : STYLE'
    p[0]=styleConv(p[1])

def p_newline(p):
    'newline : NEWLINE'
    p[0]="<br>"

def p_keyword(p):
    'keyword : KEYWORD'
    p[0]="#"+p[1]

parser=yacc.yacc()

script,file=argv
a=open(file)
b=a.read()
while(re.search(r'(image|link|list)?\([^\(\)\{\}]*?\)\{[^\(\)\{\}]*?\}',b)):
    b=parser.parse(b.strip())
b=b.split("<br>")
b="<br>\n".join(b)
print(b)
