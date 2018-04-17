#!/usr/bin/python

import sys

current_word = None
attempts = 0
success = 0
year = None
# file = "/Users/gummida/test_reduce"
# with open(file, 'r') as f:
for line in sys.stdin:
    # for line in f:
    word = line.strip().split('#')
    year = word[0]
    if word[1]=='2':
        continue
    attempts += 1
    if word[1] == '1':
        success += 1

print "%s,%d,%d" % (year, attempts, success)
