#!/bin/bash

# Una escripta simple a establecer unas cosas

sudo apt-get install curl

curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

mv ../configs/vimrc ~/.vimrc
cat ../configs/bashrc >> ~/.bashrc

mkdir -p Documents/notes
touch Documents/notes/scratchpad.md
