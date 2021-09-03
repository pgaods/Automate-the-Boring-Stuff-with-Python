#!/usr/bin/env python
# coding: utf-8

# This mini program is designed to move SAS files from one location to another automatically.

# In[69]:


import os
import shutil


# In[70]:


year='2021'


# In[71]:


def dm_Current(category):
    source = 'G:\\' + year + '\\' + category+ '\\Input Data\\'
    dest = 'G:\\' + year + '\\' + category + '\\Input Data\\Backup\\'
    
    '''Check if the files have been moved. If yes, stop the operation!'''
    os.chdir(source)
    if os.path.exists("generic filename.xlsx") == True:
        print('Backup starts...\n')
    else:
        print('Files have been backed up, no more action needed. If still needed, manually do it!\n')
        return
    
    '''Deleting all files in the Backup folder'''
    os.chdir(dest)
    files = os.listdir(dest)
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
    files = os.listdir(dest)
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
            shutil.move(source+j, dest)
    print('All files in the production folder are moved to the Backup folder\n')

