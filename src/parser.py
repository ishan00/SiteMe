import ply.yacc as yacc
from sys import argv
import re
from lexer import tokens,styles

ltaggedStyles={"bold":"b","h2":"h2","h1":"h1","h3":"h3","h4":"h4","h5":"h5","h6":"h6","italic":"i"}

def taggedMaker(style,content):
    if(not style):
        return content
    else:
        style=style.split(';')
        ltagged=[]
        htagged=[]
        for x in style:
            if(':' in x):
                htagged.append(x)
            else:
                ltagged.append(x)
        if(ltagged and htagged):
            htagged=';'.join(htagged)+';'
            ltaggedStart=''.join(['<'+ltaggedStyles[x]+'>' for x in ltagged])
            ltaggedEnd=''.join(['</'+ltaggedStyles[x]+'>' for x in ltagged[::-1]])
            return "<div style=\""+htagged+"\">"+ltaggedStart+content+ltaggedEnd+"</div>"
        elif(ltagged):
            ltaggedStart=''.join(['<'+str(ltaggedStyles[x])+'>' for x in ltagged])
            ltaggedEnd=''.join(['</'+str(ltaggedStyles[x])+'>' for x in ltagged[::-1]])
            return ltaggedStart+content+ltaggedEnd
        elif(htagged):
            htagged=';'.join(htagged)+';'
            return "<div style=\""+htagged+"\">"+content+"</div>"

def styleMaker(s):
    # styleName=re.search(r'(.*?)\(',s).group(1)
    # styleStyle=re.search(r'\((.*?)\)',s).group(1)
    # styleContent=re.search(r'\{(.*?)\}',s).group(1)
    styleName=s.split('(')[0]
    styleStyle=s.split('(')[1].split(')')[0]
    styleContent=s.split('(')[1].split(')')[1].strip('{}')
    styleStyle=styleStyle.replace(',',';')
    if(not styleName):
        rs=taggedMaker(styleStyle,styleContent)
    elif(styleName=="image"):
        if styleContent:
            rs="<img src=\"../img/"+styleContent.strip()+"\" style=\""+styleStyle.strip()+";\">"
    elif(styleName=="link"):
        if styleContent:
            if styleStyle:
                rs="<a href=\""+styleContent.strip()+"\">"+styleStyle.strip()+"</a>"
            else:
                rs="<a href=\""+styleContent.strip()+"\">"+styleContent.strip()+"</a>"
    elif(styleName=="list"):
        if styleContent:
            if styleStyle:
                rs="<"+styleStyle.strip()+"l>"+''.join(["<li>"+x+"</li>" for x in [y.strip() for y in styleContent.split('*')[1:]]])+"</"+styleStyle.strip()+"l>"
    elif(styleName=="piechart"):
        rs="\n###"+styleName+'[[['+styleStyle+']]]'+styleContent+'\n'
    # else:
    #     if styleContent:
    #         if(styleStyle=="bold"):
    #             rs="<div><b>"+styleContent+"</b></div>"
    #         elif(styleStyle[0]=='h'):
    #             rs="<div><"+styleStyle.strip()+">"+styleContent+"</"+styleStyle.strip()+"></div>"
    #         else:
    #             rs="<div>"+styleContent+"</div>"

    return rs

# def mainMaker(head,body):
#     rs="<html>\n<head>\n"+head+"\n</head>\n"+"<body>\n"+body+"\n</body>\n</html>"
#     return rs

def p_main(p):
    'main : head body'
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

def p_body(p):
    '''body : body style
            | body REST
            | body newline
            | 
    '''
    if(len(p)==3):
        p[0]=p[1]+p[2]
    else:
        p[0]=''

def p_style(p):
    'style : STYLE'
    p[0]=styleMaker(p[1])

def p_newline(p):
    'newline : NEWLINE'
    p[0]="<br>"

def p_keyword(p):
    'keyword : KEYWORD'
    if(p[1][0:3]=="###"):
        p[0]=p[1]
    else:
        p[0]="###"+p[1]

parser=yacc.yacc()

script,file=argv
a=open(file)
b=a.read()
while(re.search(r'('+'|'.join(styles)+')?\([^\(\)\{\}]*?\)\{[^\(\)\{\}]*?\}',b)):
    b=parser.parse(b.strip())
b=b.split("<br>")
b="<br>\n".join(b)
print(b)
