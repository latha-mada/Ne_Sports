#!/usr/bin/python

import sys

team = 'NE'
play = 'Pass'
conversion = 'Success'

count = 0
# required_list = [0,27,28,5,10,12,13,14]
# file = '/Users/gummida/backup/output_bak/pbp_2015.csv'
# with open(file, 'r') as f:
for line in sys.stdin:
    # for line in f:
    out = []
    word = line.strip('\n').split(',')
    year = word[0]
    if (word[27] == team or word[28] == team) and word[9] != 'NA' and word[5] == team:
        home = word[27]
        away = word[28]
        pos = word[5]
        conv = word[9]
        out.append(word[0])
        if word[9] == conversion:
            out.append(1)
        else:
            out.append(0)
    else:
        continue

    if out:
        print "%s#%d" % (out[0],out[1])
        count += 1
if count == 0:
    print "%s#%d" % (year, 2)