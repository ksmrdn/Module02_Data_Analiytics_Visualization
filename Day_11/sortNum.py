x = [3,4,5,6,7,1,2,10,80]

def urut(x):
    listUrut = []
    minX = x[0]
    i = 0
    while len(x) > 0:
            if x[i] <= minX:
                minX = x[i]
            i += 1
            if i == len(x):
                listUrut.append(minX)
                x.remove(minX)
                if x:
                    minX = x[0]
                i = 0
    print(listUrut)
urut(x)