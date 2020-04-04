#!/bin/bash

cd `dirname $0`
cat popular-names.txt | tr '\t' ' '
