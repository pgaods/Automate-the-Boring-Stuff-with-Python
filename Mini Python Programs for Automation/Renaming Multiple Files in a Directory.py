#!/usr/bin/env python
# coding: utf-8

# This mini progragram intends to rename a sequence of files in a given directory in a consistent manner. 
# 
# The following program picks out all the SAS scripts and then add a text-string prefix to each program in the front in a given directory:

# In[1]:


import os


# In[2]:


os.chdir("H:\\")
for filename in os.listdir("."):
    if filename.endswith(".sas"):
        os.rename(filename, 'AMC_'+filename)
        print('file renamed: ', filename)


# In[ ]:




