import numpy as np
'''
4x + 7y = 2
3x + 2y = -5.
Nilai 2x-3y adalah
'''
a1 = np.array([
    [4,7],
    [3,2]
])
c1 = np.array([2,-5])
b1 = np.linalg.solve(a1,c1)
print(b1)

hasil0 = b1[0]
hasil1 = b1[1]
d1 = 2*hasil0-3*hasil1
print(d1)

