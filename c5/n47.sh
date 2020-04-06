#!/bin/bash

cd `dirname $0`
LC_ALL=C sort functional_verb_constructions.txt | cut -f 1 -d $'\t' | uniq -c | sort -nr | head
echo $'\n'
LC_ALL=C sort functional_verb_constructions.txt | uniq -c | sort -nr | head
