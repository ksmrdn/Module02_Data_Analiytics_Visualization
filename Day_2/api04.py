import requests
kota = 'surabaya'
apikey = '&appid=3ac69e0b0e0a02c5c49186345f0ba92a'
url = f'http://api.openweathermap.org/data/2.5/weather?q={kota}{apikey}'
data = requests.get(url)
print(data)
print(data.json())
data = data.json()
sunrise = data['sys']['sunrise']

from datetime import datetime
utc = datetime.utcfromtimestamp(int(sunrise))
print(utc)

from dateutil import tz
myzone = tz.gettz('Asia/Jakarta')
print(utc.astimezone(myzone))