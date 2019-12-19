import requests
from bs4 import BeautifulSoup
url = requests.get('http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/')
data = BeautifulSoup(url.content,'html.parser')
print(url.status_code)
print('\n')
# print(data)
ambil = data.ul

icon = data.find_all('strong')
ultra = []
monster = []
for h in icon:
    ultra.append(h.text)
    monster.append(h.text)
print(ultra[2:36])
print('\n')
print(monster[37:110])