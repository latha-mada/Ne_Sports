#!/usr/bin/env python

"""
transfers the data files from output directory to remote vm - hadoop cluster
"""
import time
import pexpect
import os
import subprocess
user = 'hduser'
machine = 'localhost'
curr_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#curr_path = curr_path.decode()
in_path = os.path.join(curr_path, 'output')
bakup_path = os.path.join(curr_path, 'backup')
cmd = 'ls {}'.format(in_path)
timeout = time.time() + 60*60
while True:
    if time.time() > timeout:
        print("exiting the execution due to timeout")
        break
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    files = out.splitlines()
    if len(files)>0:
        for file in files:
            file_path = os.path.join(in_path, file)
            print("--- file_path = ", file_path)
            out_path = os.path.join('/home', '{}'.format(user), 'input')
            if not os.path.isdir(out_path):
               print("outpath = ", out_path)
               os.mkdir(out_path)
            print("---------- out_path = ", out_path)
            scp_cmd = 'scp {} {}@{}:/{}'.format(file_path, user, machine, out_path)
            print("----- scp_cmd = ", scp_cmd)
            pexpect.run(scp_cmd)
            # print child.before
            bak_file = os.path.basename(file_path) + '_out'
            print("bak file = ", bak_file)
            bak_file_path = os.path.join(bakup_path, bak_file)
            mv_cmd = "mv {} {}".format(file_path, bak_file_path)
            print(mv_cmd)
            pexpect.run(mv_cmd)
            # child = None
    else:
        print("There are no files to transfer. Will try in a minute")
        time.sleep(60)

