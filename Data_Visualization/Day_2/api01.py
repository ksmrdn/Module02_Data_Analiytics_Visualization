import requests # python -m pip install requests
url1 = 'http://jsonplaceholder.typicode.com/users/1'
data1 = requests.get(url1)
print(data1)
print("\n")
print(data1.json())
print("\n")
print(data1.json()['address'])
print(data1.json()['address']['suite'])
print("\n")
print(type(data1.json()))
print("\n")

url2 = 'http://jsonplaceholder.typicode.com/users'
data2 = requests.get(url2)
print(data2)
print("\n")
for i in data2.json(): 
    print(i['name'], 'at', i['address']['city'])
print("\n")
print(type(data2.json()))