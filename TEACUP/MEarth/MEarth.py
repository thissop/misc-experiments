import urllib.request, urllib.error, urllib.parse
import pandas as pd
import numpy as np
import time, progress
from progress.bar import Bar
import os, shutil
import re
import csv
#Definitions
#key = input("Paste key path: "
#teacup = input("Paste teacup path: ")
key = 'targetlist.txt'
report = './report.txt'
teacup = 'teacup/'
DR = input("Which batch would you like to query from (1/2/3/4): ")
if DR == '1':
    yf = '2008-2010'
    CAT  = './Catalogs/CAT_OBS1.csv'
    OS = 'OS1:'
#DR 2 isn't working
if DR == '2':
    yf = '2010-2011'
    CAT = './Catalogs/CAT_OBS2.csv'
    OS = 'OS2:'
elif DR == '3':
    yf = 'north2011-2018'
    CAT = './Catalogs/CAT_OBS3.csv'
    y = '2011-2018'
    OS = 'OS3:'
elif DR == '4':
    yf = 'south2014-2018'
    CAT = './Catalogs/CAT_OBS4.csv'
    OS = 'OS4:'
#Action

with open(key, 'r') as f:
    targetlist = [line.strip() for line in f]
    targetlist = list(dict.fromkeys(targetlist))
    targetlist = set(targetlist)
bar = Bar('Distillation Status:', max = len(targetlist))

def obs1_obs2():
    for elem in targetlist:
        #Actual actions for each target begins
        with open(CAT) as f: 
            f = csv.reader(f, delimiter=',')
            for line in f:
                if elem in line:
                    #gets raw
                    x = line.split(',')
                    LSPM = str(x[0])
                    TEL = str(x[2])
                    url = (batch + LSPM + '_' + TEL + '_' + yf + '.txt')
                    response = urllib.request.urlopen(url)
                    content = response.read() 
                    oldfile = ('Dirty:' + OS + LSPM + '.txt')
                    with open(oldfile,'wb') as f:
                        f.write(content)
                    #cleans and moves
                    newfile = (OS + LSPM +".txt")
                    with open(oldfile, 'r+') as of, open(newfile, 'w') as nf:
                        for line in of:
                            if '#BJD' in line:
                                colnames = line
                                colnames = colnames.replace('#BJD','BJD')
                                colnames = re.sub(' +',',',colnames)
                                licolnames = colnames.split(',')
                                licolnames = licolnames.remove('\n')
                            if '#' not in line:
                                nf.write(line)
                    os.remove(oldfile)
                    shutil.move(newfile,teacup)
                    df = pd.read_table((teacup+newfile),sep='\s+', header=None, engine='python')
                    #df.columns = licolnames
                    #df = df[['BJD','Mag','e_Mag']]
                    df = df.drop(df.columns[3:19], axis = 1)
                    df = df.round(decimals = 6)
                    open((teacup+newfile),'w').close()
                    df.to_csv((teacup+newfile), sep='\t', index = False)
                    finalfile = (teacup+newfile)
                    with open(finalfile, 'r') as fin:
                        data = fin.read().splitlines(True)
                    with open(finalfile, 'w') as fout:
                        fout.writelines(data[1:])
                #else: 
                    #with open(report,'a') as rp:
                        #rp.write(line+': None Found')

                    #prog bar
                        #with open(report, 'a')
                        bar.next()
                        time.sleep(0.01)
    time.sleep(0.01) 
def obs3():
    for elem in targetlist:
        #Actual actions for each target begins
        with open(CAT, 'r+') as f: 
            f = csv.reader(f, delimiter=',')
            for line in f:
                if elem in line:
                    #gets raw
                    x = line.split(',')
                    LSPM = str(x[0])
                    TEL = str(x[2])
                    url = (batch + LSPM + '_' + TEL + '_' + y + '.txt')
                    print(url)

                    response = urllib.request.urlopen(url)
                    content = response.read() 
                    oldfile = ('Dirty:' + OS + LSPM + '.txt')
                    with open(oldfile,'wb') as f:
                        f.write(content)
                    #cleans and moves
                    newfile = (OS + LSPM +".txt")
                    with open(oldfile, 'r+') as of, open(newfile, 'w') as nf:
                        for line in of:
                            if '#BJD' in line:
                                colnames = line
                                colnames = colnames.replace('#BJD','BJD')
                                colnames = re.sub(' +',',',colnames)
                                licolnames = colnames.split(',')
                                licolnames = licolnames.remove('\n')
                            if '#' not in line:
                                nf.write(line)
                    os.remove(oldfile)
                    shutil.move(newfile,teacup)
                    df = pd.read_table((teacup+newfile),sep='\s+', header=None, engine='python')
                    #df.columns = licolnames
                    #df = df[['BJD','Mag','e_Mag']]
                    df = df.drop(df.columns[3:19], axis = 1)
                    df = df.round(decimals = 6)
                    open((teacup+newfile),'w').close()
                    df.to_csv((teacup+newfile), sep='\t', index = False)
                    finalfile = (teacup+newfile)
                    with open(finalfile, 'r') as fin:
                        data = fin.read().splitlines(True)
                    with open(finalfile, 'w') as fout:
                        fout.writelines(data[1:])
                #else: 
                    #with open(report,'a') as rp:
                        #rp.write(line+': None Found')

                    #prog bar
                        bar.next()
                        time.sleep(0.01)
                    #fix report 
    #time.sleep(0.01) 
if DR == '1' or '2':
    batch = 'https://www.cfa.harvard.edu/MEarth/DR2/' + yf +'/lc/'
    obs1_obs2()
elif DR == '3':
    batch = 'https://www.cfa.harvard.edu/MEarth/DR8/'+ yf + '/lc/'
    obs3()
"""
                elif elem not in line:
                    with open(report, 'a') as f:
                        f.write(elem + ": Not Found")
                """      
    #Actual actions for each target ends
