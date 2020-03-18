#!/bin/zsh

cd `dirname $0`
cut -f 1 -d '	' hightemp.txt > col1sh.txt
cut -f 2 -d '	' hightemp.txt > col2sh.txt
