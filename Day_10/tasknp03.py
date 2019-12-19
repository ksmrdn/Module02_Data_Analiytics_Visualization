import numpy as np
from functools import reduce

x = [1,2,3,4,5]
y = np.array(x)

zsum = reduce(lambda a,b: a+b, x)
print(zsum)

zmin = reduce(lambda a,b: a if (a>b) else b, x)
print(zmin)

zmax = reduce(lambda a,b: a if (a<b) else b, x)
print(zmax)

print(np.mean(x))
print(np.median(x))