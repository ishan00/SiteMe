" Vim syntax file
" Language: siteme
" Maintainer: Team in the North

if exists("b:current_syntax")
	finish
endif

" Keywords
" abstractKeyword -> navbar(type){a:b,c:d,e:f}
" basicKeyword -> list(STYLE){.*}
" style
syn keyword abstractKeyword navbar footer header chatbox skillbar wallpaper parallax slideshow tooltip piechart chatbox timeline fade card grid block form modal flip shake accordian checkbox alert tooltip
syn keyword basicKeyword button table list image link piechart hover-button click-button hoverdropdown
syn keyword Negation #nonavbar #nofooter
syn keyword BinType1 title nextgroup=BinVal1 skipwhite
syn keyword BinType2 background-color color nextgroup=BinVal2 skipwhite
syn keyword BinType4 height width font-size margin margin-left margin-right nextgroup=BinVal3 skipwhite
syn keyword UnType bold italic u h1 h2 h3 h4 h5 h6 h7 danger info warning success underline center code sup sub kbd quote pre latex
syn match BinVal1 '[a-zA-Z0-9 ,.;:(){}[]@#!&/]*'
syn match BinVal2 '\(rgb[ ]*([0-9 ]*,[0-9 ]*,[0-9 ]*)\|#[0-9a-zA-Z]\+\|blue\|yellow\|red\|green\|black\|white\)'
syn match BinVal3 '\([0-9]\+\(pt\|px\)\|[0-9]\+%\)'
syn match BinVal4 '\(\b\left\b\|\b\right\b\|\bcenter\b\|\bjustified\b\)'

let b:current_syntax = "siteme"

hi def link abstractKeyword Statement
hi def link basicKeyword Statement
hi def link UnType Type
hi def link BinType1 Type
hi def link BinType2 Type
hi def link BinType3 Type
hi def link BinVal1 Constant
hi def link BinVal2 Constant
hi def link BinVal3 Constant
hi def link BinVal4 Constant
