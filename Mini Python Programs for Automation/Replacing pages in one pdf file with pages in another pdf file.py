#!/usr/bin/env python
# coding: utf-8

# In[4]:


import PyPDF2
import os
os.chdir('C:\\Users\\gao\\GAO_Jupyter_Notebook\\Automate the Boring Stuff with Python\\Datasets and Files')


# In[15]:


pdf1File = open('file A.pdf', 'rb')
pdf2File = open('file B.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter() # creating a blank PDF document here


# In[16]:


for pageNum in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]: # copy all the pages from the PDF and add them to the 'PdfFileWriter' object
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
pageObj = pdf1Reader.getPage(3)
pageObj.rotateClockwise(-90)
pdfWriter.addPage(pageObj)
for pageNum in [18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]: # copy all the pages from the PDF and add them to the 'PdfFileWriter' object
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
pdfOutputFile = open('wtf.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()


# In[ ]:




