import requests

url = 'http://quotes.rest/qod'
data = requests.get(url)
data = data.json()
print(data)