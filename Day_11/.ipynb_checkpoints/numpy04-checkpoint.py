#1
'''
Import numpy dan cek versi
'''
import numpy as np
print(np.__version__)

#2
'''
Buat 1 Dimensi array berupa nomor 0 - 9
'''
#cara 1
a1 = list(range(0,10))
a11 = np.array(a1)
print(a1)
print(a11)

#cara 2
a2 = np.arange(10)
print(a2)
print('\n')

#3
'''
Buat boolean array
'''
#cara 1
a3 = np.full((3,3), True, dtype=bool)
print(a3)

a31 = np.full((3,3), False, dtype=bool)
print(a31)

#cara 2
'''
Memberi value 1 pada seluruh elemen lalu diubah ke boolean (True)
'''
a4 = np.ones((3,3),dtype=bool)
print(a4)

'''
Memberi value 0 pada seluruh elemen lalu diubah ke boolean (False)
'''
a41 = np.zeros((3,3),dtype=bool)
print(a41)
print('\n')

#4
a5 = np.array(range(1,11,2))
print(a5)