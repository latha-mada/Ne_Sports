#!/usr/bin/python
"""
# this file will copy the data files from the source to the input folder of the app
"""
import os
import sys
import subprocess
from pathlib import Path
#sys_path = os.path.abspath(__file__)
#sys_path = os.path.join(os.path.abspath(__file__), os.pardir)
#print(sys_path)
#sys.exit(0)
sys_path = Path(__file__)
print("syspath 1 = {}".format(sys_path))
sys_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(sys_path)
sys.path.append(sys_path)
raw_file_path = os.path.join(sys_path, 'data')
cmd = 'ls {}'.format(raw_file_path)
print(cmd)
proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = proc.communicate()
out = str(out, 'utf-8')
print(out)
# do backup
nfl_files = out.splitlines()
print(nfl_files)
for i in range(len(nfl_files)):
   nfl_file = nfl_files[i]
   print("nfl file = {}".format(nfl_file))
   file1 = os.path.join(raw_file_path, nfl_file)
   print(file1)
   in_path = os.path.join(sys_path, 'input')
   print(in_path)
   if not os.path.isdir(in_path):
      os.mkdir(in_path)
   cp_cmd = 'cp {} {}/'.format(file1,in_path)
   print(cp_cmd)
   proc = subprocess.Popen(cp_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   out, err = proc.communicate()
   print(out)
