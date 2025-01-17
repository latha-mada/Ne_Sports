#!/usr/bin/env python
import os
import sys
import subprocess
import time
import re
import datetime
retain_indexes = [16, 19, 21, 23, 28, 29, 40, 42, 45]
retain_list = []
app_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
in_path = os.path.join(app_root, 'input')
out_path = os.path.join(app_root, 'output')
bak_path = os.path.join(app_root, 'backup')
print(in_path, out_path, bak_path)
cmd = 'ls {}'.format(in_path)
stop = False
count = 0
timeout = time.time() + 60*60
i = 0
while True:
    i = 1
    if time.time() > timeout:
        print("exiting the process due to timeout")
        break
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    list = out.splitlines()
    # print("list = ", list)
    if len(list) > 0:
        # print(list)
        # stop = True
        time.sleep(1)
        file_name = list[0]
        season = re.search(r'.*_(.*)\..*', file_name).group(1)
        infile = os.path.join(in_path, file_name)
        outfile = os.path.join(out_path, file_name)
        if not os.path.isdir(out_path):
            os.mkdir(out_path)
        #print(infile, outfile)
        with open(infile, 'rb') as fin, open(outfile, 'wb') as fout:
            i = 0
            for line in fin:

                if i == 0:
                    i += 1
                    #print(line)
                    # sys.exit(0)
                    continue
                else:
                    retain_list = [season]
                    # print line
                    # print("___________________")
                    # remove the description filed
                    try:
                        fields = line.split(',')
                        if fields[16]=="NA" or not bool(fields[16]):
                            print season, fields[16], fields[19], fields[21], fields[23], fields[28], fields[29]
                        if fields[28] =='NA' or fields[16]=='NA' or fields[16]=='' or fields[28] not in ['Run', 'Pass']:
                            # print fields[28]
                            continue
                        # print("length of fields = {}, {}".format(len(fields), i))
                        i += 1
                        for index in retain_indexes:

                            retain_list.append(fields[index])
                        # print(','.join(retain_list))
                        fout.write(','.join(retain_list))
                        fout.write(os.linesep)
                    except IndexError:
                        continue
                    except Exception as e:
                        print e
                        continue
        bak_file = os.path.basename(infile) + '_in'
        bak_file_path = os.path.join(bak_path, bak_file)
        print(bak_file)
        bak_cmd = 'mv {} {}'.format(infile, bak_file_path)
        print(bak_cmd)
        if not os.path.isdir(bak_path):
            os.mkdir(bak_path)
        backup = subprocess.Popen(bak_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = backup.communicate()
        print("out = {}".format(out))

    else:
        print("input is empty. Will keep polling")
        time.sleep(2)

# print path
