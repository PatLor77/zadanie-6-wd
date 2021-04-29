import numpy as np

a=np.arange(12)
b=a.reshape(3,4).flat
c=a.reshape(4,3).flat
d=a.reshape(2,6).flat

print(b)
print(c)
print(d)
#Te macierze nie są takie same