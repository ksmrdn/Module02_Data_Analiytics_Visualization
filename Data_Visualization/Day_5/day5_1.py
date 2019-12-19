from bs4 import BeautifulSoup
#web scraping from html file
data = BeautifulSoup(
        open('html_1.html', 'r'), 'html.parser'
        )
#STEP 1
# print(data.prettify())
# print('\n')
# print(data.title)
# print(data.title.name)
# print(data.title.text)
# print(data.h1.string)
# print(data.ul.text)
# print(data.ul.string)
# print(data.find_all('li'))

# ambil = data.ul
# for i in ambil.find_all('li'):
#     print(i.text)

#STEP 2
# print(data.find_all(class_='x'))
# ambil = data.ul
# for i in ambil.find_all('li',class_='sosmed'):
#     print(i.text)

#web scraping dari url
import requests
web = requests.get('http://127.0.0.1:5500/Module02/Visualisasi_Data/Day_4/html_1.html')
data = BeautifulSoup(web.content,'html.parser')
# print(data)
print(web.status_code)
# print(web.content)

ambil = data.ul
for i in ambil.find_all('li',class_='sosmed'):
    print(i.text,'\n')

for j in ambil.find_all('li',id ='social'):
    print(j.text)