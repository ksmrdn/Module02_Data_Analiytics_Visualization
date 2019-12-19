#Baca json Buat excel
import json
with open('listLagu.json','r') as z:
    out = json.load(z)
# print(out)
# print('\n')
head = list(out[0].keys())
# print(head)
data = []
for i in out:
    data.append(list(i.values()))

import xlsxwriter

file = xlsxwriter.Workbook('fromAnotherFormat.xlsx')
sheet = file.add_worksheet('json')

#write column
for i in head:
    sheet.write(0, head.index(i), i)

#write data
row = 1
for x, y, z in data:
    sheet.write(row, 0, x)
    sheet.write(row, 1, y)
    sheet.write(row, 2, z)
    row+=1

sheet1 = file.add_worksheet('csv')
#Baca csv buat excel
import csv
with open('listLagu.csv','r') as x:
    read = csv.reader(x)
    lali = list(read)

#Cara 1
# row = 0
# for x,y,z in lali:
#     sheet1.write(row, 0, x)
#     sheet1.write(row, 1, y)
#     sheet1.write(row, 2, z)
#     row+=1

#Cara 2
for i in lali:
    print(i)
    for j in i:
        print(j)
        sheet1.write(lali.index(i), i.index(j), j)
file.close()