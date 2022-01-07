import urllib.request, urllib.error, urllib.parse
import pandas as pd
import numpy as np
import time, progress
from progress.bar import Bar
import os, shutil
import re
key = '/home/thaddaeus/MY PROJECTS/Python/teacup/MEarth/targetlist.txt'
with open(key, 'r') as f:
    targetlist = [line.strip() for line in f]
    targetlist = list(dict.fromkeys(targetlist))
    targetlist = set(targetlist)
DR = input("Which batch would you like to query from (1/2/3/4): ")
#DR 2 isn't working
def obs3():
        for elem in targetlist:
        #Actual actions for each target begins
            with open(CAT, 'r+') as f: 
                for line in f:
                    if elem in line:
                        #gets raw
                        x = line.split(',')
                        LSPM = str(x[0])
                        TEL = str(x[2])
                        url = (batch + LSPM + '_' + TEL + '_' + y + '.txt')
                        response = urllib.request.urlopen(url)
                        content = response.read() 
                        oldfile = ('Dirty:' + LSPM + '.txt')
                        with open (oldfile, 'wb') as of:
                            of.write(content)
if DR == '3':
    yf = 'north2011-2018'
    CAT = '/home/thaddaeus/MY PROJECTS/Python/teacup/MEarth/Catalogs/CAT_OBS3.csv'
    y = '2011-2018'
    batch = 'https://www.cfa.harvard.edu/MEarth/DR8/'+ yf + '/lc/'
    obs3()