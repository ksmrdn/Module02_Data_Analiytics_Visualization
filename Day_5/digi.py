import requests
from bs4 import BeautifulSoup
main_url = requests.get('http://digidb.io/digimon-list/')
main_data = BeautifulSoup(main_url.content,'html.parser')
head = main_data.find_all('th')

headers = []
head_add = 'URL Icon'
for h in head:
    headers.append(h.text)
headers.append(head_add)
print(headers)

digi = main_data.find_all('td')
digimon = []
for d in digi:
    digimon.append(d.text)
print(digimon)


digi_all = []
for row in range(0,len(digimon),13):
    digi_all.append(digimon[row:row+13])
print(digi_all)

icon = main_data.find_all('img')
pics_url = []
for pic in icon:
    pics_url.append(pic['src'])
pics_url = pics_url[2:343]

for col in range(len(digi_all)):
    digi_all[col].insert(13,pics_url[col])
print(digi_all)

# list_final = []
# for i in digi_all:
#     list_final.append(dict(zip(headers,i)))
# print(list_final)

# import csv
# with open('digimon.csv','w',newline='') as out:
#     tulis = csv.DictWriter(out, fieldnames = headers)
#     tulis.writeheader()
#     tulis.writerows(list_final) 

# import xlsxwriter

# file = xlsxwriter.Workbook('digi.xlsx')
# sheet = file.add_worksheet('digiList')

# for i in headers:
#     sheet.write(0, headers.index(i), i)

# for j in range(len(digi_all)):
#     for k in range(len(headers)):
#         sheet.write(j+1, k, digi_all[j][k])
# file.close()
