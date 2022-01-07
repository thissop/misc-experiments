import urllib.request, urllib.error, urllib.parse
from urllib.error import HTTPError
import pandas as pd, numpy as ny
import os, shutil
import time, progress
from progress.bar import Bar
from tqdm import tqdm 
#Definitions
key = 'targetlist.txt'
teacup = 'teacup/'
report = 'report.txt'
grade = input('Include B class data? (Y/N): ')
magc = input("Do you want measurements from default aperture (Y/N): ")
if magc == 'N':
    specificmag = input('Which arpeture should be used? (0-4): ')
reflist = []
def add_epoch(arr):
    return ny.add(arr,epoch)
#Action
with open(key, 'r') as f:
    x = f.read().splitlines()
    x = list(set(x))
bar = Bar('Distillation Status:', max = len(x))

def dataframe():
        df = pd.read_table(final, sep = '  | |   ', header=None, engine = 'python')
        df.columns = licolnames
        df = df[['HJD',smag,smer]]
        df = df.round(decimals = 4)
        df['HJD'] = df[['HJD']].apply(add_epoch)
        open(final,'w').close()
        df.to_csv(final, sep='\t', index = False)
for element in x:
    url = str('http://www.astrouw.edu.pl/cgi-asas/asas_cgi_get_data?' + str(element) +',asas3')
    response = urllib.request.urlopen(url)
    content = response.read() 
    initial = element + '.txt'
    with open(initial,'wb') as f:
        f.write(content)
        reflist.append(initial)
        shutil.move(initial,teacup) 
        initial = teacup + initial 
        final = teacup + 'F:' + element + '.txt'
        with open(initial, 'r+') as of, open(final, 'w') as nf:
            for line in of:
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
                if '#' not in line: 
                    if grade == 'Y':
                        if 'A' in line or 'B' in line: 
                            nf.write(line.lstrip('   '))  
                    elif grade == 'N':
                        if 'A' in line: 
                            nf.write(line.lstrip('   '))
        os.remove(initial)
                
        if magc == 'Y':
            smag = licolnames[1]
            smer = licolnames[7]
            dataframe()
        elif magc == 'N':
            smag = 'MAG_' + specificmag
            smer = 'MER_' + specificmag    
            dataframe()
        
        with open(final, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(final, 'w') as fout:
            fout.writelines(data[1:])
    bar.next()
    time.sleep(0.01)   
        #bar.next()
        #time.sleep(0.01)



