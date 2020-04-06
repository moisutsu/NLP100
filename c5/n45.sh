#!/bin/bash

cd `dirname $0`
LC_ALL=C sort verb_case_patterns.txt | uniq -c | sort -nr | head

echo "「する」"
LC_ALL=C sort verb_case_patterns.txt | uniq -c | sort -nr | grep " する"

echo "「見る」"
LC_ALL=C sort verb_case_patterns.txt | uniq -c | sort -nr | grep " 見る"

echo "「与える」"
LC_ALL=C sort verb_case_patterns.txt | uniq -c | sort -nr | grep " 与える"
