import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'ksmrdn',
    passwd = '1234567',
    database = 'warehouse_rk'
)
# print(db)
cur = db.cursor()
# cur.execute('show tables')
# cur.execute('describe karyawan')
# cur.execute('select name_kar from karyawan')
# a = cur.fetchall()
def selectAll():
    cur.execute('select * from karyawan')
    x = cur.fetchall()
    print(type(x))
    for data in x:
        print(data)

b = 'insert into karyawan (name_kar, sal_kar, add_kar) values (%s, %s, %s)'
val = [("Olaf Ramli", 3000000, "JL. Kenangan II No.13"), ("Hutan Hujan", 4500000, "JL. Pinus Berduri 3 No.15")]
cur.executemany(b, val)
db.commit()
print(cur.rowcount, 'Data Tersimpan')

selectAll()

