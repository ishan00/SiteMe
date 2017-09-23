import ply.yacc as yacc
from sys import argv
import re
from lexer import tokens,styles

ltaggedStyles={"bold":"b","h2":"h2","h1":"h1","h3":"h3","h4":"h4","h5":"h5","h6":"h6","italic":"i","center":"center"}

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

def piechartMaker(style,content):
    style=style.split(';')
    r1 = re.compile("label.*")
    styleLabel = list(filter(r1.match, style))[0]
    r2=re.compile("(?!label).*")
    styleStyle=list(filter(r2.match, style))
    tempFile=open("./tmp/"+styleLabel.split(':')[1].strip()+".csv",'w')
    tempFile.write(content.replace(',','\n'))
    tempFile.close()
    file=open("./layout/GNUPlot/piechart.plot")
    newFile=open("./tmp/"+styleLabel.split(':')[1].strip()+".plot",'w')
    line=file.readline()
    templine=''
    while(line):
        if("XXXXX" in line):
            templine=templine+line.replace("XXXXX","./tmp/"+styleLabel.split(':')[1].strip()+".csv")
        elif("YYYYY" in line):
            templine=templine+line.replace("YYYYY","./site/img/"+styleLabel.split(':')[1].strip()+".png")
        else:
            templine=templine+line
        line=file.readline()
    newFile.write(templine)
    if(styleStyle):
        return "image("+','.join(styleStyle)+"){"+styleLabel.split(':')[1].strip()+".png}"
    else:
        return "image(){"+styleLabel.split(':')[1].strip()+".png}"

def imageMaker(style,content):
	if content:
		return "<img src=\"./img/"+content.strip()+"\" style=\""+style.strip()+";\">"

def linkMaker(style,content):
	if content:
		if style:
			return "<a href=\""+content.strip()+"\">"+style.strip()+"</a>"
		else:
			return "<a href=\""+content.strip()+"\">"+content.strip()+"</a>"

def listMaker(style,content):
	if content:
		if style:
			return "<"+style.strip()+"l>"+''.join(["<li>"+x+"</li>" for x in [y.strip() for y in content.split('*')[1:]]])+"</"+style.strip()+"l>"

styleFunctions={"image":imageMaker,"link":linkMaker,"list":listMaker,"piechart":piechartMaker}

def styleMaker(s):
    # styleName=re.search(r'(.*?)\(',s).group(1)
    # styleStyle=re.search(r'\((.*?)\)',s).group(1)
    # styleContent=re.search(r'\{(.*?)\}',s).group(1)
    styleName=s.split('(')[0]
    styleStyle=s.split('(')[1].split(')')[0]
    styleContent=s.split('(')[1].split(')')[1].strip('{}')
    styleStyle=styleStyle.replace(',',';')
    if(not styleName):
        return taggedMaker(styleStyle,styleContent)
    else:
    	return styleFunctions[styleName](styleStyle,styleContent)
    # else:
    #     if styleContent:
    #         if(styleStyle=="bold"):
    #             rs="<div><b>"+styleContent+"</b></div>"
    #         elif(styleStyle[0]=='h'):
    #             rs="<div><"+styleStyle.strip()+">"+styleContent+"</"+styleStyle.strip()+"></div>"
    #         else:
    #             rs="<div>"+styleContent+"</div>

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
            | body pre
            |
    '''
    if(len(p)==3):
        p[0]=p[1]+p[2]
    else:
        p[0]=''

def p_pre(p):
    '''pre : PRE 
           |  
    '''
    if(len(p)==2):
        print(p[1])
        p[0]="<pre>"+p[1][:-2][7:].replace('\n','@$$@').replace('(','^**^').replace(')','~!!~').replace('{','&--&').replace('}','+==+')+"</pre>"
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
b=b.replace('@$$@','\n').replace('^**^','(').replace('~!!~',')').replace('&--&','{').replace('+==+','}')
print(b)
