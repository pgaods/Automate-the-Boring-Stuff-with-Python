#!/usr/bin/env python
# coding: utf-8

# This program is designed to remove a specific file type in a given directory. For example, the following program removes all excel files in a given directory:

# In[2]:


import os


# In[5]:


searchpath='H:\\'
for root, dirs, files in os.walk(searchpath):
    for fname in files:
        if fname.endswith('.sas7bdat') and root==searchpath:
            print('File that will be removed: ', os.path.join(root, fname))
            os.remove((os.path.join(root, fname)))


# In[ ]:




