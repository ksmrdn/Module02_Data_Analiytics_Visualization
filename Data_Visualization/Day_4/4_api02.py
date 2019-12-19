import requests
a = input('Makan apa: ')
b = a.split(' ')
eat = '%20'.join(b)

url = f'https://developers.zomato.com/api/v2.1/search?entity_id=74&entity_type=city&q={eat}'

apikey = '94ccd365dba11b2318f40110946a9aaf'
headInfo = {
    'user-key': apikey
    }

data = requests.get(url, headers=headInfo)
resto = data.json()['restaurants']
for i in range(len(resto)):
    nama = resto[i]['restaurant']['name']
    locate = resto[i]['restaurant']['location']
    location = locate['adress']
    print(f'{i+1}, Nama reto: {nama}\n Lokasi: {location}')