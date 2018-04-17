#!/usr/bin/python

import sys

team = 'NE'
play = 'Pass'
passerID = '00-0019596'
i = -1
required_list = [0,27,28,5,10,12,13,14]
# file = '/Users/gummida/backup/output_bak/pbp_2014.csv'
# with open(file, 'r') as f:
for line in sys.stdin:
    # for line in f:
    out = []
    word = line.strip('\n').split(',')
    if (word[27] == team or word[28] == team) and word[10] ==play and word[12] == passerID and word[5] == team:
        home = word[27]
        away = word[28]
        play = word[10]
        passID = word[12]
        pos = word[5]
        out.append(word[0])
        if word[14] == 'Complete':
            out.append(1)
        else:
            out.append(0)
    else:
        continue

    print "%s#%d" % (out[0],out[1])
