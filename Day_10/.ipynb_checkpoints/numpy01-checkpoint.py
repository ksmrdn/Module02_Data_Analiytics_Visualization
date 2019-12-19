import numpy as np
x1 = [1,2,3,4,5]
y1 = np.array(x1)
print(x1[::2])
print(y1[::2])
print(x1+x1)
print(y1+y1)
print('\n')

x2 = [
    [1,2,3],
    [4,5,6]
    ]
y2 = np.array(x2)
print(x2[0][1])
print(y2[1,1]) #y[1][1]
print(y2.ndim) #di dalam list ada list
print('\n')

x3 = [[[1,2,3],[4,5,6],[7,8,9]]]
y3 = np.array(x3)
print(y3)
print(y3.ndim)
print(y3.size)
print(y3.dtype)
print(y3.itemsize) #byte 
print(y3.shape)
print('\n')

x3 = [[[1,2,3,4,5],[4,5,6,7,8],[7,8,9,10,11]]]
y3 = np.array(x3)
print(y3.shape)
print('\n')

x4 = np.arange(1,10,2)
print(list(range(1,10,2)))
print(len(x4))
print('\n')

print(np.random.random(10)) #angka random 10 bilangan 0 - 1
print(np.random.rand(2,4)) #2 elemen 4 bilangan
print(np.random.randint(7,size = (2,5))) #2 elemen 5 bilangan, tanpa 7
print('\n')

#spacing
print(np.linspace(1,5,5))
print(np.linspace(1,100,5))
print('\n')

x5 = [(1,2,3),(4,5,6),(7,8,9)]
y5 = np.array(x5)
# print(y5[0,2])
# print(y5[0:2, 0:2])
# print(y5[0:, 0:2])
print(y5[0:,0:1]) #size=3 shape(3,1)
print(y5[0:,:1].reshape(3,))
print(y5[0:3,0]) #size=3 shape=(3,)
print(y5[0:3,0].reshape(3,1))
# print(y5[0:,1:2])
# print(y5[0:3,1])
# print(y5[0:,[0,-1]])
print('\n')

a = np.array([
    [0,-7],
    [-1,3]
])

b = np.array([
    [2,4],
    [3,8]
])

print(a+b)
print('\n')
print(a-b)
print('\n')
print(a*b)
print('\n')
print(a+2)
print('\n')
c = np.array([1,2,3,4])
c[0] += 2
print(c)
print('\n')

'''
3x = 6
'''
a2 = np.array([3]).reshape(1,1) #atau
# a2 = np.array([[3]])
c2 = np.array([6])
b2 = np.linalg.solve(a2,c2)
print(int(b2))
print('\n')

'''
2x + y = 5
 x + y = 7
SPLDV
'''

a1 = np.array([
    [2,1],
    [1,1]
])

c1 = np.array([5,7])
b1 = np.linalg.solve(a1,c1)
print(b1)
print('\n')

