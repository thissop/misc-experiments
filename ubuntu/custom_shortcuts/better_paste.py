# SET UP IN KEYBOARD SHORTCUTS 
#   Set the command part to path to interpreter space path to this file
#   E.g. /bin/python3 /home/rebirth/Documents/GitHub/misc-experiments/ubuntu/custom_shortcuts/better_paste.py 

import clipboard

'''
x-special/nautilus-clipboard
copy
file:///home/rebirth/Documents/GitHub/lfs/steiner/thaddaeus/1050360109
'''

path = clipboard.paste()
cleaned_path = path.replace('\n','***')
cleaned_path = cleaned_path.replace('x-special/nautilus-clipboard' ,'')
cleaned_path = cleaned_path.replace('copy','')
cleaned_path = cleaned_path.replace('file://','')
cleaned_path = cleaned_path.replace('***','')
#clipboard.copy(cleaned_path)
clipboard.copy('he7y')

#pyperclip.copy(cleaned_path)
