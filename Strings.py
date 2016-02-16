# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 02:53:28 2016

@author: bhuvan
"""

data=['a','b','c']
strlist = []
for i in range(9):
    if i%2==0:
        strlist.append(i)
    else:
        strlist.clear()
        strlist.append("Stuck")
print(strlist)