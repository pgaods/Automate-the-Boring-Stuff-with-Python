#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ask the user to enter the names of files to compare
fname1 = input("Enter the first filename: ")
fname2 = input("Enter the second filename: ")


# In[2]:


# Open file for reading in text mode (default mode)
import string
f1 = open(fname1)
f2 = open(fname2)
elist=['SAS', 'cpu', 'NOTE:', 'real time', 'WARNING:']


# In[3]:


# Read the first line from the files
F1_line = f1.readline()
F2_line = f2.readline()

try:
    firstdigits1=str([int(s) for s in F1_line.split() if s.isdigit()][0])
    f1_line=F1_line.replace(firstdigits1, "")
except IndexError:
    f1_line=F1_line

try:
    firstdigits2=str([int(s) for s in F2_line.split() if s.isdigit()][0])
    f2_line=F2_line.replace(firstdigits2, "")
except IndexError:
    f2_line=F2_line
    

# Initialize counter for line number
line_no = 1

# Print confirmation
print("-----------------------------------")
print("Comparing files: ", " v1: " + fname1, " v2: " + fname2, sep='\n')
print("-----------------------------------\n")

# Loop if either file1 or file2 has not reached EOF
print("Instruction:")
print("--If a line does not exist on the file, we mark the output with + sign.")
print("--Otherwise we output the line on the other file and mark it with a v1/v2 sign.\n")

while (f1_line != '' or f2_line != ''):
    
    if f1_line.strip() != f2_line.strip():
        
        # If a line does not exist on file2 then mark the output with + sign
        if f2_line == '' and f1_line != '':
            if all([s not in f1_line for s in elist]):
                print("v2+", "Line-%d:" % line_no, f1_line)
            else:
                pass

        # otherwise output the line on file1 and mark it with v2 sign
        elif f1_line != '':
            if all([s not in f1_line for s in elist]):
                print("v2", "Line-%d:" % line_no, f1_line)
            else:
                pass
            
        # If a line does not exist on file1 then mark the output with + sign
        if f1_line == '' and f2_line != '':
            if all([s not in f2_line for s in elist]):
                print("v1+", "Line-%d:" % line_no, f2_line)
            else:
                pass
            
        # otherwise output the line on file2 and mark it with v1 sign
        elif f2_line != '':
            if all([s not in f2_line for s in elist]):
                print("v1", "Line-%d:" %  line_no, f2_line)
            else:
                pass 

        # Print a blank line
        print()

    #Read the next line from the file
    F1_line = f1.readline()
    F2_line = f2.readline()
    
    try:
        firstdigits1=str([int(s) for s in F1_line.split() if s.isdigit()][0])
        f1_line=F1_line.replace(firstdigits1, "")
    except IndexError:
        f1_line=F1_line

    try:
        firstdigits2=str([int(s) for s in F2_line.split() if s.isdigit()][0])
        f2_line=F2_line.replace(firstdigits2, "")
    except IndexError:
        f2_line=F2_line
    
    #Increment line counter  
    line_no += 1

f1.close()
f2.close()

# References:
# http://www.opentechguides.com/how-to/article/python/58/python-file-comparison.html (Python SCRIPT)
# http://psych.colorado.edu/~carey/courses/psyc7291/SASExamples/anova.example.sas (SAS CODE)


# In[ ]:




