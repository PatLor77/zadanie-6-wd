import numpy as np

a=np.arange(9).reshape(3,3)
b=np.arange(16).reshape(4,4)
def findSmallestInRowCol(a):
    answer = "Najmniejsze wartości w poszczególnych rzędach macierzy to: \n"
    for x in a:
      answer+= str(np.amin(x)) + "\n"
      a = a.T
    answer+="Najmniejsze wartości w poszczególnych kolumnach macierzy to: \n"
    for y in a:
        answer+=str(np.amin(y)) + "\n"
    return answer
print(findSmallestInRowCol(a))
print(findSmallestInRowCol(b))