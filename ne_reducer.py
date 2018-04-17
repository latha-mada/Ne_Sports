#!/usr/bin/python

import sys

current_word = None
passyards = 0
rushyards = 0
touchdowns = 0
two_pt = 0
# file = "mapper_out.csv"
# with open(file, 'r') as f:
for line in sys.stdin:
    # for line in f:
        word = line.strip().split('#')
        if current_word:


            # print word
            if word[0] == current_word:
                key = word[0]
                # print key
                value_list = word[1].split('~')
                passyards += int(value_list[0])
                rushyards += int(value_list[1])
                touchdowns += int(value_list[2])
                two_pt += int(value_list[3])
            else:
                if (passyards+rushyards+touchdowns+two_pt) > 0: 
                    print("{},{},{},{},{}".format(current_word.replace('~', ','), passyards, rushyards, touchdowns, two_pt))
                current_word = word[0]
                value_list = word[1].split('~')
                passyards = int(value_list[0])
                rushyards = int(value_list[1])
                touchdowns = int(value_list[2])
                two_pt = int(value_list[3])
        else:
            current_word = word[0]
            value_list = word[1].split('~')
            passyards = int(value_list[0])
            rushyards = int(value_list[1])
            touchdowns = int(value_list[2])
            two_pt = int(value_list[3])

