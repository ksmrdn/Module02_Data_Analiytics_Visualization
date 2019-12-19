import numpy as np

#SWAP
x0 = np.arange(1,10).reshape(3,-1)
print(x0)
print(x0[:,[1,0,2]]) #seluruh dimensi, swap tiap matrix jadi diisi elemen 1 elemen 0 elemen 2
print(x0[:,[0,0,0]])
print(x0[[1,0,2], :]) #seluruh dimensi di swap

#Transpose
x1 = np.array([[1,2],[3,4],[5,6]])
print(x1)
print(x1.transpose())

x2 = np.loadtxt('0.csv', skiprows=1, delimiter=',', unpack=True)
print(x2)
#skiprows -> skip row pertama
#delimiter -> split with coma and combine it
#unpack -> memisahkan tiap kolom

# id, usia = np.loadtxt('0.csv', skiprows=1,delimiter=',',unpack=True)
# print(id)
# print(usia)
# np.savetxt('1.csv', usia, fmt='%d',header='usia', comments='')

data = np.loadtxt('0.csv', skiprows=1,delimiter=',')
np.savetxt('1.csv', data, fmt='%d',header='ID, USIA', comments='', delimiter=',')

# id, usia = np.loadtxt('0.csv', skiprows=1,delimiter=',',unpack=True)
# data1 = np.array(list(map(lambda a,b: [a,b], id, usia)))
# print(data1)

# np.savetxt('1.csv', data1, fmt='%d', header='ID, USIA', comments='', delimiter=',')