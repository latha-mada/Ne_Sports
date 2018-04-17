#!/usr/bin/env python

import sys

team = 'NE'
play = 'End of Game'
i = -1
required_list = [0,5,6,8,10,13,14,25,26,27,28]
#file = '/home/hduser/backup/pbp_2013.csv'
#with open(file, 'r') as f:
for line in sys.stdin:
#  for line in f:
    out = []
    i += 1
    word = line.strip('\n').split(',')
    #print(word, len(word))
    if (word[28] == team):
        #print(word[28])
        home = word[27]
        away = word[28]
        posscore = word[25]
        defescore = word[26]
        pos = word[5]
        out.append(word[0])
        #print("\n\n   -------------", word[28])
        if word[28] == 'NE':
            out.append('HOME')
           # print("at home")
        else:
            out.append('AWAY')
           # print("away")
        try:
            posscore = int(word[25])
            defscore = int(word[26])
           # print("poss = {}, def = {}".format(posscore, defscore))
        except:
           # print("------------I am continuing")
            continue

        if word[5] == team:
           # print("word[25] = {}, word[26] = {}".format(word[25], word[26]))
            score = int(word[25]) - int(word[26])
            if score > 0:
                out.append(1)
            else:
                # i += 1
                continue
        else:
            score = int(word[26]) - int(word[25])
            if score > 0:
                out.append(1)
            else:
                # i += 1
                continue

        #print "%s%s#%d" % (out[0],out[1], out[2])
        print("{}{}#{}".format(out[0],out[1],out[2]))
