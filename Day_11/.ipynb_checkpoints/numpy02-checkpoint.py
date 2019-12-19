import numpy as np
from functools import reduce

x = [[1,20,3,400,5],[3,5,7,9,10]]
y = np.array(x)

# zsum = reduce(lambda a,b: a+b, x)
# print(zsum)

# zmin = reduce(lambda a,b: a if (a>b) else b, x)
# print(zmin)

# zmax = reduce(lambda a,b: a if (a<b) else b, x)
# print(zmax)

print(np.mean(x))
print(np.median(x))
print(np.argmax(y))
print(np.argmin(y))
print(y.shape)
print(y.reshape(-1))
print(y.reshape(2,-1))

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[0,0,0],[0,0,0]])
c = np.zeros((2,3),dtype = 'int32')
print(c.dtype)
print(c)

a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
b1 = np.ones((3,3))
print(a1*b1)

a2 = np.zeros((3,3), dtype = bool)
print(a2)

a3 = np.zeros((3,3), dtype=bool)
print(a3)
print('\n')

lain = np.full((1,3), 'Dia')
print(lain)
print(type(lain))
print(lain.tolist())
print(type(lain.tolist()))
ca = np.array(a)
ba = np.array(b)
c0 = [a,b]
c1 = np.array(a+b).reshape(2,-1).tolist()
c2 = np.concatenate([[ca],[ba]], axis = 0).tolist()
c3 = np.vstack([ca,ba])
print(c1)
print(c2)
d1 = np.arange(1,11)
d2 = np.where(d1%2 != 0, 0, d1)
print(d2)

print(np.where(d1<9))
print(d2[np.where(d1<9)])
print(d2[np.where((d1>3)&(d1<9))])
print(d1[(d1>3)&(d1<9)])

y1 = np.array([[1,2,1],[3,3,1],[2,1,2]])
print(y1)
print(np.linalg.det(y1))

y2 = np.array([[3,2],[1,4]])
print(y2)
y3 = np.linalg.inv(y2)

#dotproduct
print(y2@np.linalg.inv(y2))
print(y2.dot(np.linalg.inv(y2)))
print(y2 @ y3)

#cross product x
print(np.cross(y2,y2))
print(y2*y3)