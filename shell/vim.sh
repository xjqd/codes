#!/bin/bash
(mkdir -p ~/.vim/autoload ~/.vim/bundle && git clone https://github.com/tpope/vim-pathogen.git )
if (($? != 0 ))
then
   exit 1
fi
mv ./vim-pathogen/autoload/* ~/.vim/autoload
rm -rf ./vim-pathogen

cat >> ~/.vimrc <<- EOF
execute pathogen#infect()
syntax on
filetype plugin indent on
EOF
