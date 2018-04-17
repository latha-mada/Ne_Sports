#!/usr/bin/python
import sys
import os
import csv
# path to the django project which has setting.py file"
django_path = "/home/latha/my_django/mysite/mysite"
print(sys.path)
sys.path.append(django_path)
print(sys.path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()
from nesports.models import MlbData

csv_path = "/home/latha/my_django/mysite/mlb.csv"

data = csv.reader(open(csv_path), delimiter=',', quotechar='"')
for row in data:
    if row:
        mod = MlbData()
        mod.year = row[0]
        mod.team = row[2]
        mod.player = row[1]
        mod.games = row[3]
        mod.homeplate = row[4]
        mod.homeruns = row[5]
        mod.walks = row[6]
        mod.save()
