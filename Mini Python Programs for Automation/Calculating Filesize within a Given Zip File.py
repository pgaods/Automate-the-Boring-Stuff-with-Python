#!/usr/bin/env python
# coding: utf-8

# We create an independent mini-program now to get the zip file information for every single file and subfolder in the zip file. Once you specify the path of the zip file and the name of the zip file, we can get their file size information for each file and subfolder in that particular zip file.
# 
# The program only needs to params from the user: 'filedir' and 'fname'. The 'filedir' tells Python where the zip file is, and the 'fname' tells what the zip file is (e.g. zippedupfile.zip).

# In[2]:


import zipfile,os
filedir='C:\\Users\\GAO\\Anaconda\\Scripts\\Gao_Jupyter_Notebook_Python_Codes\\Datasets and Files' # zip file location
fname='zipexample.zip' # zip file name

os.chdir(filedir) # move to the folder with the zip file 'example.zip'
exampleZip = zipfile.ZipFile(fname)
print('These are the individual files and folders within the current zip file: \n' + str(exampleZip.namelist()))
print('\n-----------------------------------------------------------------------\n')

flist=exampleZip.namelist()
for i in flist:
    fileinzip = exampleZip.getinfo(i) # getting information within the zip file
    print(fileinzip.filename)
    print('Original Size of ' + str(fileinzip.file_size) + ' KB')
    print('After compression, it has ' + str(fileinzip.compress_size) + ' KB')
    try:
        print('Compressed file is %sx smaller!' % (round(fileinzip.file_size / fileinzip.compress_size, 2)))
    except ZeroDivisionError:
        print('The original file/folder is 0KB already, nothing to be compressed')
    print('')
    exampleZip.close()


# In[ ]:




