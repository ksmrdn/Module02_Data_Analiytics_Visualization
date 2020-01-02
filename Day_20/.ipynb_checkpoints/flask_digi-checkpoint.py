from flask import Flask, jsonify, send_from_directory, render_template, abort
server = Flask(__name__)
import requests
from bs4 import BeautifulSoup
main_url = requests.get('http://digidb.io/digimon-list/')
main_data = BeautifulSoup(main_url.content,'html.parser')
head = main_data.find_all('th')

headers = []
head_add = 'URL Icon'
for h in head:
    headers.append(h.text.replace('#','NO'))
headers.append(head_add)
print(headers)

digi = main_data.find_all('td')
digimon = []
for d in digi:
    digimon.append(d.text.replace('\xa0',''))
# print(digimon)


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
# print(digi_all)

#Home route
@server.route('/')
def home():
    return render_template('digi_table.html', 
    header = headers,
    data = digi_all
    )

@server.route('/listJson')
def listJson():
    dictDigi = []
    for i in digi_all:
        tempList = dict(zip(headers,i))
        dictDigi.append(tempList)
    print(tempList)
    return jsonify(dictDigi)

#dynamic root: student/1
@server.route('/listJson/<int:NO>')
def eachDigi(NO):
    dictDigi = []
    for i in digi_all:
        tempList = dict(zip(headers,i))
        dictDigi.append(tempList)
    if NO > len(digi_all) or NO < 1:
        abort(404)
    else:
        return jsonify(dictDigi[NO-1])

#route untuk error
@server.errorhandler(404)
def notFound(error):
    return render_template('error.html')

if __name__ == '__main__':
    server.run(debug = True)