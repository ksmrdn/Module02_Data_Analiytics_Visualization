from flask import Flask, jsonify, send_from_directory, render_template, abort, redirect, request
import mysql.connector as mc

app = Flask(__name__)

#Connect to sql
dbsql = mc.connect(
    host='localhost', 
    user='ksmrdn', 
    passwd = '1234567',
    database='testing'
)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def form():
    if request.method == 'POST':
        body = request.form
        x = dbsql.cursor()
        data = (body['nama'], body['usia'])
        sql = f'insert into datadiri (nama, usia) values {data}'
        x.execute(sql)
        dbsql.commit()
        return redirect('/data')

@app.route('/data', methods=["GET","POST"])
def data():
    
    if request.method == 'GET':
       #Cara 1
        # x = dbsql.cursor()
        # x.execute('select * from datadiri')
        # result = x.fetchall()
        # result = list(map(lambda i: {'id':i[0],'nama':i[1],'usia':i[2]}, result))
      #Cara 2
        x = dbsql.cursor(dictionary=True)
        x.execute('select * from datadiri')
        result = x.fetchall()
        print(result)
        return jsonify(result)
    elif request.method == 'POST':
        body = request.json
        x = dbsql.cursor()
        data = (body['nama'],body['usia'])
        query = f'insert into datadiri (nama,usia) values {data}'
        x.execute(query)
        dbsql.commit()
        return 'POST' 

@app.route('/data/<int:no>', methods=["GET","POST"])
def datum(no):
        x = dbsql.cursor(dictionary=True)
        query = f'SELECT * FROM `datadiri` WHERE `ID` = {no}'
        x.execute(query)
        result = x.fetchall()
        print(result)
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=1998)
