#!/bin/bash

cd `dirname $0`
split -l $1 popular-names.txt split
