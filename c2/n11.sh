#!/bin/zsh

cd `dirname $0`
cat hightemp.txt | tr '\t' ' '
