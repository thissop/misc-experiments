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
key = input("Paste key path: ")
teacup = input("Paste teacup path: ")
print("  ")
grade = input("Do you want B grade data as well as A grade data? (Y/N): ")
print("   ")
magc = input("Do you want measurements from default aperture (Y/N): ")
print("   ")
if magc == 'N':
    specificmag = input("Do you want measurements from a specific aperture (Y/N): ")
    if specificmag == 'Y':
        chosenmag = input("Enter aperture (0,1,2,3,4): ")
        smag = ("MAG_"+chosenmag)
        smer = ("MER_"+chosenmag)
inclerr = input("Do you want to include mag err as third column (Y/N): ")
print("   ")
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
    #print(initial) 
    p = (element + '.txt')
    totea.append(p)
#moves file to distillation folder 
for element in totea:
    shutil.move(element,teacup)
def add_epoch(arr):
    return ny.add(arr,epoch)
#distills 
for elem in totea:
    truefile = (teacup + elem)
    bluefile = (teacup+"FINAL_"+elem)
    with open(truefile) as oldfile, open(bluefile, 'w') as newfile:
        for line in oldfile:
            if '# -  HJD-' in line:
                epoch = line
                epoch = epoch.replace('# -  HJD-','')
                epoch = float(epoch)
            if '#     HJD      ' in line:
                colnames = line
                colnames = colnames.replace('#     HJD      ', 'HJD ')
                colnames = colnames.replace('    ', ' ')
                colnames = colnames.replace('  ',' ')
                colnames = colnames.replace('HJDMAG', 'HJD MAG')
                licolnames = colnames.split(' ')
                licolnames.insert(6,'TAB')            
            if '#' not in line: #Gets rid of everything in file except data (e.g. descriptors)
                if grade == 'Y':
                    if 'A' in line or 'B' in line: #Cleans data, keeps 'A' and 'B' class data only
                        newfile.write(line.lstrip('   ')) #Strips pesky leftover left whitespace 
                elif grade == 'N':
                    if 'A' in line: 
                        newfile.write(line.lstrip('   '))
    oldfile.close
    newfile.close
    if magc == 'N':
        if inclerr == 'N':
            df = pd.read_table((teacup+"FINAL_"+elem), sep = '  | |   ', header=None, engine = 'python')
            df.columns = licolnames
            df = df[['HJD',smag]]
            df = df.round(decimals = 4)
            df['HJD'] = df[['HJD']].apply(add_epoch)
            open((teacup+"FINAL_"+elem),'w').close()
            df.to_csv((teacup+"FINAL_"+elem), sep='\t', index = False)
        
        elif inclerr == 'Y':
            df = pd.read_table((teacup+"FINAL_"+elem), sep = '  | |   ', header=None, engine = 'python')
            df.columns = licolnames
            df = df[['HJD',smag,smer]]
            df = df.round(decimals = 4)
            df['HJD'] = df[['HJD']].apply(add_epoch)
            open((teacup+"FINAL_"+elem),'w').close()
            df.to_csv((teacup+"FINAL_"+elem), sep='\t', index = False)
    elif magc == 'Y':
        defmag = licolnames[1]
        defmer = licolnames[6]
        if inclerr == 'N':
            df = pd.read_table((teacup+"FINAL_"+elem), sep = '  | |   ', header=None, engine = 'python')
            df.columns = licolnames
            df = df[['HJD',defmag]]
            df = df.round(decimals = 4)
            df['HJD'] = df[['HJD']].apply(add_epoch)
            open((teacup+"FINAL_"+elem),'w').close()
            df.to_csv((teacup+"FINAL_"+elem), sep='\t', index = False)
        
        elif inclerr == 'Y':
            df = pd.read_table((teacup+"FINAL_"+elem), sep = '  | |   ', header=None, engine = 'python')
            df.columns = licolnames
            df = df[['HJD',defmag,defmer]]
            df = df.round(decimals = 4)
            df['HJD'] = df[['HJD']].apply(add_epoch)
            open((teacup+"FINAL_"+elem),'w').close()
            df.to_csv((teacup+"FINAL_"+elem), sep='\t', index = False)
#Deletes old file (with raw asas)
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
