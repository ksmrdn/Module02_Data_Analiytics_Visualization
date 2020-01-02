import xlrd
import xlsxwriter
#Baca Excel
file = xlrd.open_workbook('fromAnotherFormat.xlsx')
sheet = file.sheet_by_index(0)
sheet1 = file.sheet_by_index(1)

list1 = []
for row in range(sheet.nrows):
    out = sheet.row_values(row)
    list1.append(out)
print(list1)
print('\n')
head = list1[0]

list2 = []
for row1 in range(sheet1.nrows):
    out1 = sheet1.row_values(row1)
    list2.append(out1)
print(list2)
print('\n')

a = ['Gleen Fredly','Kasih Putih',2006], ['Sandy Sandoro','Malam Biru',2012], ['Kangen Band','Bintang 14 Hari',2008]
for z in a:
    list1.append(z)
print(list1)
list3 = list1[1:]
print(list3)
# list2 = []
# for row in list1:
#     list2.append(dict(zip(list1[0], row)))
# list3 = list2[1:]
# print(list2)

#Tulis Excel

file = xlsxwriter.Workbook('fromAnotherFormat.xlsx')
sheet2 = file.add_worksheet('json')
sheet3 = file.add_worksheet('csv')

for y in head:
    sheet2.write(0, head.index(y), y)

for i in list3[1:]:
    for j in i:
        sheet2.write(list3.index(i), i.index(j), j)

for a in list2:
    for b in a:
        sheet3.write(list2.index(a), a.index(b), b)
file.close()
# row = 11
# col = 0
# for x, y, z in list1[1:]: 
#         sheet.write(row, col, a)
#         sheet.write(row, col, b)
#         row+=1
#         col+=1
# file.close()