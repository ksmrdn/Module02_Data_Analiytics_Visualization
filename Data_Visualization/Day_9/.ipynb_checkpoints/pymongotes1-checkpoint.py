import pymongo
# import datetime as dt

dburl = 'mongodb://localhost:27017'
mymongo = pymongo.MongoClient(dburl)

dbs = mymongo.list_database_names()
print(dbs)

mydb = mymongo['pymongodb']
mycol = mydb['colmong']

alldata1 = list(mycol.find())
# alldata2 = list(mycol.find({'nama': 'Andi'}, {'nama': 1}))
# alldata3 = list(mycol.find({'usia': {'$gt': 24}}))
print(alldata1)
# print(alldata3)

# mydata1 = {'nama': 'Deni', 'usia': 18, 'kota': 'Kediri'}
# print(mycol.insert_one(mydata1))

# mydata2 = [
#             {'nama': 'Deni', 'usia': 18, 'kota': 'Kediri'},
#             {'nama': 'Eulis', 'usia': 23, 'kota': 'Surabaya'},
#             {'nama': 'Fino', 'usia': 26, 'kota': 'Nganjuk'}
#             ]
# x1 = mycol.insert_many(mydata2)
# print(x1.inserted_ids)

# nama = ['Andi','Caca','Fino']
# x2 = list(mycol.find({'nama': {'$in': nama}}))
# print(x2)

# x3 = mycol.insert_one({'nama':'Cinta'})
# print(x3.inserted_id)
# print(list(mycol.find({'_id': x3.inserted_id})))

# x4 = {'nama': 'Deni'}
# mycol.delete_one(x4)
# mycol.delete_many(x4)

# data1 = {'nama': 'Eulis'}
# new1 = {'nama': 'Silue'}
# mycol.update_one(data1, {'$set': new1})

# data2 = {'$and': 
#         [{'usia': {'$gt':21}}, 
#         {'usia': {'$lt':30}}]
#         }
# new2 = {'nama': 'Tralala'}
# mycol.update_many(data2, {'$set': new2})

mydb = mymongo ['jule']
mycol = mydb['julea']
# mycol.insert_one({'nama':'pop'})

# mycol.insert_one({
#     'nama':'New', 'time': dt.datetime.utcnow()
#     })

import pytz
jkt = pytz.timezone('Asia/Jakarta')
q = mycol.find({'nama': 'New'},{'time':1})
print(list(q)[0]['time'])

q1 = mycol.find({'nama': 'New'},{'time':1})
print(jkt.localize(list(q1)[0]['time']))
