#!/bin/bash

cd `dirname $0`
LC_ALL=C sort -n popular-names.txt | uniq -w 6
