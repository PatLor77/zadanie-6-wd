import numpy as np

def addMatrix(a, b):
     if a.shape == b.shape:
         sum = np.add(a, b)
         print(sum)
     else :
         print("Matrix size do not match")

a=np.arange(6).reshape(2,3)
b=np.arange(6).reshape(3,2)
addMatrix(a,b)

