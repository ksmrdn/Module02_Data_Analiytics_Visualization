#Excel to Json & CSV
import xlrd
import json
file = xlrd.open_workbook('ListLagu.xlsx')
#sheet = file.sheet_by_index(0)
sheet = file.sheet_by_index(0)
print(sheet.nrows, sheet.ncols)
#print(sheet.nrows, sheet.ncols)
# print(sheet.cell_value(0,0))
# print(sheet.cell_value(0,1))
# print(sheet.cell_value(0,2))

#nama kolom difile xlsx
# for i in range(sheet.ncols):
#     print(sheet.cell_value(0,1))

#nama kolom di file xlsx
cols = []
# for i in range(sheet.ncols):
#     cols.append(sheet.cell_value(0,i))
# print(cols)
print(sheet.row_values(0))


list1 = []
for row in range(sheet.nrows):
    out = sheet.row_values(row)
    list1.append(out)
print(list1)
print("=========================")

list2 = []
for row in list1:
    list2.append(dict(zip(list1[0], row)))
list2 = list2[1:]
print(list2)

with open('listLagu.json', 'w') as y:
    json.dump(list2,y)

import csv
with open('listLagu.csv','w',newline='') as ex:
    # header = list1[0]
    header = list(list2[0].keys())
    tulis = csv.DictWriter(ex, fieldnames = header)
    tulis.writeheader()
    tulis.writerows(list2)