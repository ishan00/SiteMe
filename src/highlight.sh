if [ ! -d "~/.vim/" ]
        then
        mkdir ~/.vim
fi

if [ ! -d "~/.vim/syntax/" ]
        then
        mkdir ~/.vim/syntax
fi

if [ ! -f "~/.vim/syntax/sm.vim" ]
        then
        cp sm.vim ~/.vim/syntax/
fi

if [ ! -d "~/.vim/ftdetect/" ]
        then
        mkdir ~/.vim/ftdetect
fi

if [ ! -f "~/.vim/ftdetect/sm.vim" ]
        then
        touch ~/.vim/ftdetect/sm.vim
        echo "au BufRead,BufNewFile *.sm set filetype=sm" >~/.vim/ftdetect/sm.vim
fi

