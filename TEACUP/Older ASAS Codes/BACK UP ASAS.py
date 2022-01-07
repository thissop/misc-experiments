key = '/home/thaddaeus/asasnames.txt'
teacup = '/home/thaddaeus/teacup/'
grade = 'Y'
import urllib.request, urllib.error, urllib.parse
import pandas as pd, numpy as ny
import os, shutil
#Welcome
print(" ")
print("Hi! Let's get some ASAS data!")
print(" ")
print("Begin by pasting the path for the key (text file with object identifiers).")
print("Then paste the path for the 'teacup' file (the folder into which data will be distilled).") 
print(" ")
#Definitions 
#key = input("Paste key path: ")
#teacup = input("Paste teacup path: ")
print("  ")
#grade = input("Do you want B grade data as well as A grade data? (Y/N): ")
print("   ")
inclerr = 'N'
#inclerr = input("Do you want to include mag err as third column (Y/N): ")
#Action
with open(key, 'r') as f:
    x = f.read().splitlines()
totea = []
for element in x:
    url = str('http://www.astrouw.edu.pl/cgi-asas/asas_cgi_get_data?' + str(element) +',asas3')
    response = urllib.request.urlopen(url)
    content = response.read() 
    f = open((element + '.txt'),'wb')
    f.write(content)
    initial = (element+".txt")
    f.close
    print(initial) 
    p = (element + '.txt')
    totea.append(p)
#moves files from directory that they naturally go in (the one this .py is in) and puts them in new file for cleaning
for element in totea:
    shutil.move(element,teacup)
#Turns previous list into a list of file names
#Cleans all data files by pasting data that meets requirements into new file
for elem in totea:
    truefile = (teacup + elem)
    bluefile = (teacup+"FINAL_"+elem)
    with open(truefile) as oldfile, open(bluefile, 'w') as newfile:
        for line in oldfile:
            if '#' not in line: #Gets rid of everything in file except data (e.g. descriptors)
                if grade == 'Y':
                    if 'A' in line or 'B' in line: #Cleans data, keeps 'A' and 'B' class data only
                        newfile.write(line.lstrip('   ')) #Strips pesky leftover left whitespace 
                elif grade == 'N':
                    if 'A' in line: 
                        newfile.write(line.lstrip('   '))
    oldfile.close
    newfile.close
#opens data as data frame, keeps what was the MAG_0 data column only (so I can plug the files into peranso)
    if inclerr == 'N':
        df = pd.read_table((teacup+"FINAL_"+elem), sep = '  | |   ', header=None, engine = 'python')
        df = df.drop(df.columns[2:14], axis=1)
        df = df.round(decimals = 3)
        open((teacup+"FINAL_"+elem),'w').close()
        df.to_csv((teacup+"FINAL_"+elem), sep='\t', index = False)
    """
    NEED TO FIX, INCLUDE MAG ERR IF WANTED

    elif inclerr == 'Y':
        df = pd.read_table((teacup+"FINAL_"+elem), sep = '  | |   ', header=None, engine = 'python')
        df = df.drop(df.columns[2:4], axis=1)
        df = df.drop(df.columns[2:14], axis=1)
        df = df.round(decimals = 3)
        open((teacup+"FINAL_"+elem),'w').close()
        df.to_csv((teacup+"FINAL_"+elem), sep='\t', index = False)
"""
#Deletes old, 'dirty' files, keeps cleaned data files only 
for elem in totea:
    truefile = (teacup+ elem)
    os.remove(truefile)
#Deletes that pesky dataframe artifact in row one 
    finalfile = (teacup+"FINAL_"+elem)
    with open(finalfile, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(finalfile, 'w') as fout:
        fout.writelines(data[1:])
print(" ")
print("Distillation complete...*sip tea*")
