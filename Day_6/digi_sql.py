import requests
from bs4 import BeautifulSoup
import mysql.connector

main_url = requests.get('http://digidb.io/digimon-list/')
main_data = BeautifulSoup(main_url.content,'html.parser')
head = main_data.find_all('th')

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'ksmrdn',
    passwd = '1234567',
    database = 'digimon'
)
ab = db.cursor()

def selectAll():
    ab.execute('select * from digimon_list')
    x = ab.fetchall()
    print(type(x))
    for data in x:
        print(data)

# headers = []
# head_add = 'URL Icon'
# for h in head:
#     headers.append(h.text)
# headers.append(head_add)
# print(headers)

digi = main_data.find_all('td')
digimons = []
for d in digi:
    digimons.append(d.text)
# print(digimons)

digi_all = []
for row in range(0,len(digimons),13):
    digi_all.append(digimons[row:row+13])
# print(digi_all)

icon = main_data.find_all('img')
pics_url = []
for pic in icon:
    pics_url.append(pic['src'])
pics_url = pics_url[2:343]

for col in range(len(digi_all)):
    digi_all[col].insert(13,pics_url[col])
print(digi_all)


'''
HTML -> SQL
-> Melakukan web scraping
    'http://digidb.io/digimon-list/'
-> Mendapatkan list seluruh element
    digi_all
-> Buat Database dalam SQL
    create database 'digimon'
-> Buat Table dalam phpmyadmin
-> Buat headers dalam phpmyadmin
-> insert into (headers) values (%s)
-> Masukkan isi dari table
-> perulangan looping baris per 14 kolom dalam 341 baris
-> insert tables and values
-> execute 
-> commit
-> rowcount
'''

# def cont(x):
#     for baris in digi_all:
#         print(listdigi.append[baris])
#         for kolom in baris:
#             listdigi.append[kolom]
#             print(listdigi)

ins = 'insert into digimon_list (HASHTAG, DIGIMON, STAGE, TYPE, ATTR, MEMORY, EQUIP_SLOTS, HP, SP, ATK, DFN, INTEL, SPEED, URL) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
val = digi_all
ab.executemany(ins, val)
db.commit()
print(ab.rowcount, 'Data Tersimpan')

selectAll()