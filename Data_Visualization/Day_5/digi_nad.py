import requests
from bs4 import BeautifulSoup as bs
import mysql.connector

myDB = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = 'nadian',
    passwd = 'nadian',
    database = 'pwd_digimon'
)

print(myDB)
myCursor =  myDB.cursor()

def selectAllDigimon():
    sql = 'select * from digimon'
    myCursor.execute(sql)
    x =  myCursor.fetchall()
    print(type(x))
    for data in x:
        print(data)

url = "http://digidb.io/digimon-list/"
dataDigimon = requests.get(url).content
# print(dataultra)
dataDigimon = bs(dataDigimon,'html.parser')

listDigi = []
temList = []
for i in dataDigimon.find_all('td'):
    cek = str(i.text)
    print(cek, end = ' ')
    if cek[0]== ' ': 
        print('y')
    
    temList.append(cek.replace('\xa0', '')) # replace some noise character
    counter += 1 
    # get each row by counting the column. end the nCols is 13
    if (counter%13==0):
        listDigi.append(temList)
        temList =[]
        print()
        counter = 0
        
for i in listDigi:
    print(i)