import numpy as np

'''
2 buku tulis, 1 pensil, 1 penghapus = 4700
1 buku tulis, 2 pensil, 1 penghapus = 4300
3 buku tulis, 2 pensil, 1 penghapus = 7100

2x + y + z = 4700
x + 2y + z = 4300
3x + 2y + z = 7100

Berapa 1 buku tulis, 1 pensil, 1 penghapus
'''
a = np.array([
    [2,1,1],
    [1,2,1],
    [3,2,1]
])

b = np.array([4700,4300,7100])
c = np.linalg.solve(a,b)
print(c)

x = c[0]
y = c[1]
z = c[2]
print(int(c[0]+c[1]+c[2]))
print(int(x+y+z))

