import numpy as np
import math

M = np.zeros(shape=(6,6), dtype=float)
M[3][0]=1
M[1][1]=1
M[4][1]=1
M[4][2]=1
M[1][2]=1
M[2][3]=1
M[4][3]=1
M[0][4]=1
M[3][4]=1
M[2][5]=1
M[3][5]=1
M[0][0]=1
print(M)

def shortestPath(A,i,j,n):
    if i==n-1 and j == n-1:
        return A[i][j]
    elif i == n-1:
        return A[i][j]+shortestPath(A,i,j+1,n)
    elif j == n-1:
        return A[i][j]+shortestPath(A,i+1,j,n)
    else:
        return A[i][j] + min (shortestPath(A,i,j+1,n),shortestPath(A,i+1,j,n)) 

P=shortestPath(M,0,0,6)
print(P)
