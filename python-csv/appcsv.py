import csv
import os
import pdb

with open('deepin-appstore-app-list.csv', 'rb') as csvfile:
    spam = csv.reader(csvfile)
    for row in spam:
        cmd = "apt-cache search %s"%(row[2])
#        print("%s|%s"%(row[1],row[2]))
#        pdb.set_trace()
