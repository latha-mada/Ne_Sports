#!/usr/bin/python

import sys

i = -1
required_list = [0,27,28,5,10,12,13,14]
#file = '2017.csv'
#with open(file, 'r') as f:
for line in sys.stdin:
# for line in f:
    out = []
    word = line.strip('\n').split(',')
    if word[5]=='Run':
        try:
            rushyards = int(word[2])
            passyards = 0
            touchdown = int(word[3])
            if word[4] != "NA":
                two_pt = 1
            else:
                two_pt = 0
            player = word[7]
        except:
            continue
    else:
        try:
            rushyards = 0
            passyards = int(word[2])
            touchdown = int(word[3])
            if word[4] != "NA":
                two_pt = 1
            else:
                two_pt = 0
            player = word[6]
        except:
            continue
    out_key = "{}~{}~{}".format(word[0], word[1], player)
    out_value = "{}~{}~{}~{}".format(passyards, rushyards, touchdown, two_pt)

    print("{}#{}".format(out_key,out_value))
