# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 01:32:30 2016

@author: bhuvan
"""

class Matrix:
    def __init__(self, mat, nrows, ncolumns):
        """Initialize matrix so that it contains all 0s
        
        nrows, ncolumns: positive integers
        """
        # Insert your code here
        self.mat=mat        
        self.nrows=nrows
        self.ncolumns=ncolumns
        
        
    def shape(self):
        """Returns the number of rows and columns (as a tuple)"""
        # Insert your code here
        Shap=[]
        Shap.append(len(self.mat))
        Shap.append(len(self.mat[0]))
        print("Shape",Shap)
        return Shap # Remove this! 
        
    def getitem(self, row, col):
        """Returns the element value at given position
        
        If indices are not in range, raise an 
        IndexError exception
        
        row,col: non-negative integers
        """
        try:
            Item=self.mat[row][col]
            # Insert your code here
            return Item 
        except:
            print("That is out of range of the defined Matrix")        
                
        
    def setitem(self, row, col, value):
        """Set the matrix element at given position value
        
        If indices are not in range, raise an 
        IndexError exception
        
        row, col: non-negative integers
        value: float
        """
        # Insert your code here
        try:
            self.mat[row][col]=value
            print(self.mat)
        except:
            print("That is out of range of the defined Matrix")
        
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
        #Initializing the To be Slicing matrix
        Sl=[]
        for i in range(0,r_end-r_start):
            Sl.append([])
            for j in range(0,c_end-c_start):
                Sl[i].append(0)
        #Collecting the slicing matrix
        for i in range(r_start,r_end):
            # Loop over columns.
            for j in range(c_start,c_end):
                Sl[i-r_start][j-c_start]=self.mat[i][j]
                print(self.mat[i][j], end="")
        print(end="\n")
        return Sl # Remove this!
     
    def scaleBy(self, factor):
        """Multiply each element by the given factor
        
        The matrix is modified by this operation
        
        factor: float
        """
        # Insert your code here
        #Initializing the To be Scaled matrix
        Sc=[]
        for i in range(0,len(self.mat)):
            Sc.append([])
            for j in range(0,len(self.mat[0])):
                Sc[i].append(0)
        
        for i in range(0,len(self.mat)):
            for j in range(0,len(self.mat[0])):
                    Sc[i][j]=factor*self.mat[i][j]
        print(Sc)
        return Sc
        
    def transpose(self):
        """Creates and returns a new matrix obtained by 
        transposing the matrix, i.e. interchanging rows 
        and columns.
        """
        # Insert your code here
        print("Transposed Matrix")        
        for i in range(0,self.ncolumns):
            for j in range(0,self.nrows):
                print(self.mat[j][i], end="")
            print(end="\n")
        
      
    def add(self, other):
        """Creates and returns a new matrix obtained 
        by adding this matrix to other using +
        
        If matrices are not compatible for addition, 
        raise a TypeError exception
        
        other: Matrix
        """
        # Insert your code here
        # Initializing the Resultant Matrix
        A=[]
        for i in range(0,len(self.mat)):
            A.append([])
            for j in range(0,len(self.mat[0])):
                A[i].append(0)
        #Exception Handling Block
        try:        
            if len(self.mat)!=len(other):
                raise TypeError()
            elif len(self.mat[0])!=len(other[0]):
                raise TypeError()
            else:
                for i in range(0,len(self.mat)):
                    for j in range(0,len(self.mat[0])):
                        A[i][j]=self.mat[i][j]+other[i][j]
                print("Addition",A)
        except:
            print("The  Matrices are not compatible;enter compatible matrix")
        return A 

       
    def sub(self, other):
        """Creates and returns a new matrix obtained 
        by subtracting other from this matrix using -
        
        If matrices are not compatible for subtraction, 
        raise a TypeError exception
        
        other: Matrix
        """
        # Insert your code here
        # Initializing the Resultant Matrix
        Sub=[]
        for i in range(0,len(self.mat)):
            Sub.append([])
            for j in range(0,len(self.mat[0])):
                Sub[i].append(0)
        try:        
            if len(self.mat)!=len(other):
                raise TypeError()
            elif len(self.mat[0])!=len(other[0]):
                raise TypeError()
            else:
                for i in range(0,len(self.mat)):
                    for j in range(0,len(self.mat[0])):
                        Sub[i][j]=self.mat[i][j]-other[i][j]
                print("Subtraction",Sub)
        except:
            print("The  Matrices are not compatible;enter compatible matrix")       
        return Sub 


       
    def mul(self, other):
        """Creates and returns a new matrix obtained by 
        multiplying this matrix with other using *
        
        If matrices are not compatible for multiplication, 
        raise a TypeError exception
        
        other: Matrix
        """
        # Insert your code here
        # Initializing the Resultant Matrix
        m=[]
        for i in range(0,len(self.mat)):
            m.append([])
            for j in range(0,len(self.mat[0])):
                m[i].append(0)
        try:        
            if len(self.mat)!=len(other[0]):
                raise TypeError()
            elif len(self.mat[0])!=len(other):
                raise TypeError()
            else:        
                for i in range(0,len(self.mat)):
                    for j in range(0,len(other[0])):
                        m[i][j]=0
                        for k in range(len(self.mat[0])):
                            m[i][j]=m[i][j]+self.mat[i][k]*other[k][j]
                print("Result of multiplication",m)
        except:
            print("The  Matrices are not compatible;enter compatible matrix")       
        return m         


MatImp=Matrix([[1,2,3],[4,5,6]],2,3)
s=MatImp.shape()
I=MatImp.getitem(1,0)
MatImp.setitem(0,0,5)
y=MatImp.getslice(0,1,0,2)
sf=MatImp.scaleBy(3)
MatImp.transpose()
A=MatImp.add([[1,2,3,4],[4,5,6,4]])
Sub=MatImp.sub([[1,2,3],[1,1,6]])
Mul=MatImp.mul([[1,2],[1,1],[3,4]])
print(s)
print(I)
print(y)
print(sf)
print(A)
print(Sub)
print(Mul)
#print(MatImp)



