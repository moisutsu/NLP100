#!/bin/bash

cd `dirname $0`
cut -f 1 -d '	' popular-names.txt > col1sh.txt
cut -f 2 -d '	' popular-names.txt > col2sh.txt
