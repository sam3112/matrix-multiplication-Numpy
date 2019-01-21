n1,m2=1,0
while n1!=m2: #checks if multiplication possible(from matrix theory)
 print('enter the size of first matrix m1xn1\n')
 m1,n1=int(input('m1= ')),int(input('n1= ')) # user input for size of 1st matrix
 print('enter the size of second matrix m2xn2\n')
 m2,n2=int(input('m2= ')),int(input('n2= '))#user input size of 2nd matrix
 if n1!=m2:
  print('"oops entered wrong sizes of matrices try againe  "')
from numpy import * # importing numpy module
print('1st matrix')
a=zeros(m1*n1)                          #1st matrix 'a' initialized as flat zeros matrix
for i in range(m1*n1):                  #for loop for user input for elements of matrix a
    a[i]=int(input('enter elements'))
a= a.reshape(m1,n1)                     #reshaping the flat matrix to user intended matrix
print('2nd matrix')
b=zeros(m2*n2)                          #2nd matrix 'b' initialized as flat zeros matrix
for i in range(m2*n2):
    b[i]=int(input('enter elements '))  #same as first matrix
b= b.reshape(m2,n2)                     #same as first matrix
c=zeros(m1*n2)                 #initializing result c matrix as zeros matrix of size m1xn2
n=0                            #index counter for resultant matrix
for i in range(m1):            #nested for loop for matrix multiplication
    for j in range(n2):
        s=0
        for k in range(n1):
            s=s+a[i,k]*b[k,j]
        c[n]=s
        n=n+1
print(a)
print(b)
print(c.reshape(m1,n2))       #reshaping the flat matrix to result matrix shape m1xn2
print(matrix(a)*matrix(b))
