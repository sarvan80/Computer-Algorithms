# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 01:05:17 2016

@author: bhuvan
"""
#!/usr/bin/python

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return mylist

# Now you can call changeme function
mylist = [10,20,30];
s=changeme( mylist );
print("Values outside the function: ", mylist)
print(s)
