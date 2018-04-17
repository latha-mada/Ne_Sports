#!/usr/bin/env python

"""
This file is used to store the files from local directory ~/input to hdfs /user/vagrant/app/data/<season>

"""
import os
import pexpect
import subprocess
import re
import time
import sys
hdfs_cmd = 'hdfs dfs'
input_path = os.path.join('/', 'home', 'hduser', 'input')
backup = os.path.join('/', 'home', 'hduser', 'backup')
cmd = 'ls {}'.format(input_path)
timeout = time.time() + 60*1 # times out after 1 hour
while True:
    if time.time() > timeout:
        print("The execution of stored timed out. Exiting....")
        break
    proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    files = out.splitlines()
    if len(files)>0:
        for file in files:
            print("------------file = ", file)
            season = re.search(r'.*_(.*)\..*', file).group(1)
            print season
            hdfs_path = os.path.join('/user', 'hduser', 'app', 'data', season)
            mkdir = '{} -mkdir -p {}'.format(hdfs_cmd, hdfs_path)
            file_path = os.path.join(input_path, file)
            put_cmd = '{} -put {} {}'.format(hdfs_cmd, file_path, hdfs_path)
            pexpect.run(mkdir)
            time.sleep(2)
            print("Copying {} to hdfs".format(file_path))
            pexpect.run(put_cmd)
            print("Copied....")
            if not os.path.isdir(backup):
                print("backup dir not exists. Creating backup")
                print("---------backup dir = ", backup)
                pexpect.run('mkdir -p {}'.format(backup))
            pexpect.run('mv {} {}'.format(file_path, backup))
            time.sleep(6)
    else:
        print("There are no files to copy to hdfs. Checking after 60secs")
        time.sleep(6)



