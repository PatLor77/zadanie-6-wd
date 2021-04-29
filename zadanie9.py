import numpy as np

a=np.arange(81).reshape(9,9)
print(a)
print(a.reshape(1,81))
print(a.reshape(3, 27))