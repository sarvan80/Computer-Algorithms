# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 03:32:20 2016

@author: bhuvan
"""
#1st part
print("test")
#Initializing 1st Matrix
x=[]
for i in range(0,2):
    x.append([])
    for j in range(0,3):
        x[i].append(0)
print(x)

# Finding the row & Column length of the Array
Shape=[]
Shape.append(len(x))
Shape.append(len(x[0]))
print("Shape",Shape)
   
# Finding the colum length of the Array
print("length",len(x[0])) 
#2nd part
print(x[1][1])

# 3rd Part
for i in range(1,2):
    for j in range(0,2):
        x[i][j]=1
print(x)
x[1][1]=23
#y=x

# 4th Part-Slicing 
for i in range(0,2):
    # Loop over columns.
    for j in range(0,3):
        
            print(x[i][j], end="")
    print(end="\n")

#Transpose

#Scaling eg by 2
#Initializing the To be Scaled matrix
Sc=[]
for i in range(0,len(x)):
    Sc.append([])
    for j in range(0,len(x[0])):
        Sc[i].append(0)
print(Sc)

for i in range(0,len(x)):
    for j in range(0,len(x[0])):
            Sc[i][j]=2*x[i][j]
print(Sc)

#Addition
z=x
A=[]
for i in range(0,len(x)):
    A.append([])
    for j in range(0,len(x[0])):
        A[i].append(0)
print(A)

for i in range(0,len(x)):
    for j in range(0,len(x[0])):
            A[i][j]=x[i][j]+z[i][j]
print("Addition",A)

#Subtraction
Sub=[]
for i in range(0,len(x)):
    Sub.append([])
    for j in range(0,len(x[0])):
        Sub[i].append(0)
print(Sub)

for i in range(0,len(x)):
    for j in range(0,len(x[0])):
            Sub[i][j]=x[i][j]-Sc[i][j]
print("Subtraction",Sub)
  
#Multiplication

#Initializing 2nd Matrix
y=[]
for i in range(0,3):
    y.append([])
    for j in range(0,2):
        y[i].append(0)
print("y",y)

for i in range(0,2):
    for j in range(0,2):
        y[i][j]=1
print("Modified y",y)

#Transpose
print("Transpose")
for i in range(0,3):
    # Loop over columns.
    for j in range(0,2):
        #y[j][i]=x[j][i]
        print(x[j][i], end="")
    print(end="\n")


m=[]
for i in range(0,2):
    m.append([])
    for j in range(0,2):
        m[i].append(0)
print(m)

#Resultant of the Multiplication
for i in range(0,len(x)):
    for j in range(0,len(y[0])):
        m[i][j]=0
        for k in range(len(x[0])):
            m[i][j]=m[i][j]+x[i][k]*y[k][j]
print(m)


'''
class Matrix:
    def __init__(self, nrows, ncolumns):
        """Initialize matrix so that it contains all 0s
        
        nrows, ncolumns: positive integers
        """
        # Insert your code here
        
    def shape(self):
        """Returns the number of rows and columns (as a tuple)"""
        # Insert your code here
        return (-1,-1) # Remove this! 
        
    def getitem(self, row, col):
        """Returns the element value at given position
        
        If indices are not in range, raise an 
        IndexError exception
        
        row,col: non-negative integers
        """
        # Insert your code here
        return 0 # Remove this! 

    def setitem(self, row, col, value):
        """Set the matrix element at given position value
        
        If indices are not in range, raise an 
        IndexError exception
        
        row, col: non-negative integers
        value: float
        """
        # Insert your code here
        
    def getslice(self, r_start, r_end, c_start, c_end):
        """Returns sub-matrix consisting of the rows
        r_start, r_start+1, ... r_end-1 and the columns
        c_start, c_start+1, ... c_end-1
        
        If indices are not in range or ill-specified, 
        raise an IndexError exception. For instance, 
        0 <= r_start < r_end and 0 <= c_start < c_end 
        must be true.
        
        r_start, r_end: slice of rows
        c_start, c_end: side of columns
        """
        # Insert your code here
        return Matrix(1,1) # Remove this!
        
    def scaleBy(self, factor):
        """Multiply each element by the given factor
        
        The matrix is modified by this operation
        
        factor: float
        """
        # Insert your code here
        
    def transpose(self):
        """Creates and returns a new matrix obtained by 
        transposing the matrix, i.e. interchanging rows 
        and columns.
        """
        # Insert your code here
        
        
    def __add__(self, other):
        """Creates and returns a new matrix obtained 
        by adding this matrix to other using +
        
        If matrices are not compatible for addition, 
        raise a TypeError exception
        
        other: Matrix
        """
        # Insert your code here
        return Matrix(1,1) # Remove this!

        
    def __sub__(self, other):
        """Creates and returns a new matrix obtained 
        by subtracting other from this matrix using -
        
        If matrices are not compatible for subtraction, 
        raise a TypeError exception
        
        other: Matrix
        """
        # Insert your code here
        return Matrix(1,1) # Remove this!

        
    def __mul__(self, other):
        """Creates and returns a new matrix obtained by 
        multiplying this matrix with other using *
        
        If matrices are not compatible for multiplication, 
        raise a TypeError exception
        
        other: Matrix
        """
        # Insert your code here
        return Matrix(1,1) # Remove this!
'''
#MatImp=Matrix([[1,2,3],[4,5,6]],2,3)

        