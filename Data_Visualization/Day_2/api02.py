import requests
klub = input('Ketik nama klub: ')
url1 = 'http://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='
data1 = requests.get(url1+klub)
players = data1.json()['player']

for player in players:
    # print(player['strPlayer'])
    print(f"{player['strPlayer']} ({player['strPosition']})")
