import os,sys
# simple file name finder with python 

file_scanned = []
file_found = [] 


def mencari(value_dir,target): 
    try:
        for value_name in os.listdir(value_dir): # get list directory/files from input
            full_value = os.path.join(value_dir,value_name) # joining value_name and value_dir
            file_scanned.append(full_value)
            sys.stdout.write('\r({}) Scanned Founded({})'.format(len(file_scanned),len(file_found)))
            if os.path.isdir(full_value):
                mencari(full_value,target) # looping for finding files again 
            else:
                if target == value_name:
                    #print('Found ',full_value)
                    file_found.append(full_value)
        sys.stdout.flush()
    except FileNotFoundError:
        exit('Directory Not found')

#mencari('..','run.py')
'''
Found  ../flasky-blog/run.py
Found  ../bot_telegram/run.py
Found  ../filter-upload/run.py
Found  ../wordlist-generator/run.py
Found  ../flask-blog/run.py
Found  ../simple-crud/run.py
Found  ../simpleencode/run.py
'''

target = input('File Name to find : ')
value_dir = input('Dir to Scan : ')

mencari(value_dir,target)

if len(file_found) != 0:
    print('\n')
    for _ in file_found:
        print(_)
else:
    exit('File Not Found')