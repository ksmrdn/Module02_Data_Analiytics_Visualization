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
file.close()

# import xlsxwriter
# file = xlsxwriter.Workbook('JsonToExcel.xlsx')
# sheet1 = file.add_worksheet('Melow')
# for i in range(sheet1.nrows):
#     for j in range(sheet1.ncols):
#         sheet1.write(i,j,out[])
