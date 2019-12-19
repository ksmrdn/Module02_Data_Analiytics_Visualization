import requests
#Mencari seluruh nama pemain dalam suatu klub
url1 = 'http://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='
klub = input('Ketik nama klub: ')
data1 = requests.get(url1+klub)
players1 = data1.json()['player']
if players1 == None:
    print("Invalid")
else:
    for data1 in players1:
        print(data1)

# for player in players1: 
#     print(f"{player['strPlayer']} ({player['strPosition']})")

#Mencari nama seorang nama
url2 = 'http://www.thesportsdb.com/api/v1/json/1/searchplayers.php?p='
pemain = input('Ketik nama pemain: ')
data2 = requests.get(url2+pemain)
players2 = data2.json()['player']
if players2 == None:
    print("Invalid")
else:
    for plyr in players2:
        print(plyr)
