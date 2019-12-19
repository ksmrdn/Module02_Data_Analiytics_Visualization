import mysql.connector

myDB = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'ksmrdn',
    passwd = '1234567',
    database = 'warehouse_rk'
)

a = myDB.cursor(dictionary=True)
# print(list(map(lambda x: x[0], out)))

# q2 = 'insert into karyawan (name_kar) values (%s)'
# nama = ('Flora Bowie',)
# a.execute(q2, nama)
# myDB.commit()

# q3 = 'delete from karyawan where name_kar = %s'
# nama = ('Olaf Ramli',)
# a.execute(q3,nama)
# myDB.commit()

# q4 = 'update karyawan set name_kar = %s where name_kar = %s'
# nama = ('Fiersa Besari','Hutan Hujan')
# a.execute(q4,nama)
# myDB.commit()

# q5 = 'update karyawan set add_kar = %s where id_kar = %s'
# nama = ('JL. Ende Flore 5',11)
# a.execute(q5,nama)
# myDB.commit()

q6 = 'alter table karyawan add column hobby varchar(255)'
# nama = ('JL. Ende Flore 5',11)
a.execute(q6)
myDB.commit()

q = 'select name_kar from karyawan'
a.execute(q)
out = a.fetchall()

print(out)
