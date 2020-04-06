#!/bin/bash

cd `dirname $0`
sort -r -t "	" -k 3 -n popular-names.txt
