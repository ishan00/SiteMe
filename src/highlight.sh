if [ ! -d "~/.vim/" ]
        then
        mkdir ~/.vim
fi

if [ ! -d "~/.vim/syntax/" ]
        then
        mkdir ~/.vim/syntax
fi

if [ ! -f "~/.vim/syntax/siteme.vim" ]
        then
        cp siteme.vim ~/.vim/syntax/
fi

if [ ! -d "~/.vim/ftdetect/" ]
        then
        mkdir ~/.vim/ftdetect
fi

if [ ! -f "~/.vim/ftdetect/siteme.vim" ]
        then
        touch ~/.vim/ftdetect/siteme.vim
        echo "au BufRead,BufNewFile *.siteme set filetype=siteme" >~/.vim/ftdetect/siteme.vim
fi

