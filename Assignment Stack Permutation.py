# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:42:31 2016

@author: bhuvan
"""


def stackPermutationTrace(n, seq):
    """Returns the sequence of push, pop and pass moves 
    if seq is a stack permutation, else return ['stuck']
    
    n: positive integer
    seq: a permutation of [0,1,...,n-1] as a list
    """
    class Stack:
        def __init__(self):
            self.items = []
        def is_empty(self):
            return self.items == []
        def push(self, item):
            self.items.insert(0, item)
        def pop(self):
            return self.items.pop(0)
        def peek(self):
            if self.items == []:
                print("The stack is empty")
                return 0
            else:
                return self.items[0]
                
        def size(self):
            return len(self.items)
        def pas(self,item):
            self.items.insert(0, item)
            return self.items.pop(0)
    

    print(n,seq)
    strlist = []
    l=[]
    i=0
    while i<len(n):
        print(n[i])
        s = Stack()
        for j in range(len(seq)):
            if n[i]==seq[j]:
                strlist.append("Pass")
                l.append(seq[j])
                s.pas(seq[j])
                #seq[j]=0
                i=i+1
            else:
                strlist.append("Push")
                s.push(seq[j])
                #Checking the stack
            c=1
            while c>0:
                if i<len(n):
                    if n[i]==s.peek():
                        l.append(s.pop())
                        strlist.append("Pop")
                        i=i+1
                    else:
                        c=0     
                else:
                    c=0     
    print(l,n,seq)
    if l!=n:
        strlist.clear()
        strlist.append("Stuck")
    return strlist    

    # Insert code here
    # Possible permutations = (2 1 0), (0 1 2), (1 0 2), (0 2 1) and (1 2 0).
    
    #return ['push','pop','stuck','pass'] # Remove this!
A=stackPermutationTrace([0,1,3,2],[0,1,2,3])
print("The Trace sequence",A)


# Inputs from the class
# usage of Break point
#Usage of the continue statement
# usage of else for loop







