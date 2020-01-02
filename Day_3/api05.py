# 1. get api sportsdb, daftar pemain suatu klub
# 2. input: klub
# 3. daftar pemain: nama, posisi, usia, negara
# 4. save X.xlsx, X.json, X.csv

import requests
import datetime as dt
time = dt.datetime.now()
tahun1 = str(time).split(' ')
tahun2 = tahun1[0].split('-')
print(tahun2)
tahun3 = int(tahun2[0])

klub = input('Ketik nama klub: ')
url = 'http://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='
data = requests.get(url+klub)
players = data.json()['player']

# for age in usia:
#     umur = tahun2 - age
# print(umur)

for player in players:
    lahir = player['dateBorn'].split('-')
    thnLahir = int(lahir[0])
    for usia in lahir:
        umur = tahun3 - thnLahir  
        print(f"Name: {player['strPlayer']}, Position: {player['strPosition']}, Age: {player(umur)}")
