#Baca Excel tulis Excel Baru
import xlsxwriter
import xlrd

file = xlrd.open_workbook('ListLagu.xlsx')
sheet = file.sheet_by_index(0)
list1 = []
for row in range(sheet.nrows):
    out = sheet.row_values(row)
    list1.append(out)
print(list1)
print('\n')

list2 = []
for row in list1:
    list2.append(dict(zip(list1[0], row)))
list3 = list2[1:]
print(list2)
head = list1[0]
file = xlsxwriter.Workbook('ListLaguRev.xlsx')
sheet1 = file.add_worksheet('Melow')

# Cara 1
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        sheet1.write(i,j,list1[i][j])
file.close()
print("==================================================")

#Cara 2
#write column
# for i in head:
#     sheet1.write(0, head.index(i), i)

#write data
# row = 0
# for x, y, z in list1:
#     sheet1.write(row, 0, x)
#     sheet1.write(row, 1, y)
#     sheet1.write(row, 2, z)
#     row+=1
# file.close()