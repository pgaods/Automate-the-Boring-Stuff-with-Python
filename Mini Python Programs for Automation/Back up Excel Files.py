#!/usr/bin/env python
# This mini program is designed to move output files from one location to another automatically. Run only once!

import os
import shutil
year='2021'

def dm_Current(folder):
    source = 'G:\\' + year + '\\' + folder + '\\' + 'prod\\'
    destin = 'G:\\' + year + '\\' + folder + '\\' + 'prod\\Backup\\'
    
    '''Check if the files have been moved. If yes, stop the operation!'''
    os.chdir(source)
    if os.path.exists("myfile_name.xlsx") == True:
        print('Backup starts...\n')
    else:
        print('Files have been backed up, no more action needed. If still needed, manually do it!\n')
        return
    
    '''Deleting all files in the Backup folder'''
    os.chdir(destin)
    files = os.listdir(destin)
    for f in files:
        if f.endswith('xlsx'):
            #print(f)
            os.remove(f)
    for f in files:
        if f.endswith('xlsx.bak'):
            #print(f)
            os.remove(f)
    print('All files in the Backup folder are cleaned')

    '''Deleting all bak files in the prod folder'''
    os.chdir(source)
    files = os.listdir(source)
    for f in files:
        if f.endswith('xlsx.bak'):
            #print(f)
            os.remove(f)
    print('All bak files in the production folder are cleaned')
    
    '''moving all excel files to the Backup folder'''
    os.chdir(source)
    files = os.listdir(source)
    for j in files:
        if j.endswith('xlsx'):
            #print(j)
            shutil.move(source+j, destin)
    print('All files in the production folder are moved to the Backup folder\n')

# dm_Current('myfolder')





