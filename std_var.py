import numpy as np



 # make a matrix of 3 by 3 filled with zeros
 
mat = [[ 0 for i in range(2)] for j in range(2)]
print(mat)
a=[[1,2],
   [4,-5]]

b=[[5,6],
   [8,21]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            mat[i][j]+= a[i][k]*b[k][j]
print(mat)