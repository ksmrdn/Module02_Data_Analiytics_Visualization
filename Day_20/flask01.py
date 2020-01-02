from flask import Flask, jsonify, send_from_directory, render_template, abort
server = Flask(__name__)

#Home route
@server.route('/')
def home():
    return '<h1>Berhasil Hore</h1>'

#render html
@server.route('/tryGet')
def tryGet():
    return render_template('tryGet.html')

#send data from flask, render html
@server.route('/data')
def data():
    nama = 'Rachmad'
    kota = 'Surabaya'
    return render_template(
        'data.html',
        data={'name':nama, 'city': kota}
    )

student = [{"id":0,"nama":"Ksmrdn","usia":21,"kota":"Surabaya"},
       {"id":1,"nama":"Ksmrdna","usia":22,"kota":"Surabaya"},
       {"id":2,"nama":"Ksmrdni","usia":23,"kota":"Surabaya"},
       {"id":3,"nama":"Ksmrdnu","usia":24,"kota":"Surabaya"},
       {"id":4,"nama":"Ksmrdno","usia":25,"kota":"Surabaya"}]

#route response json
@server.route('/std')
def std():
    return jsonify(student)
 
#dynamic root: student/1
@server.route('/std/<int:id>')
def murid(id):
    if id > len(student)-1 or id < 0:
        abort(404)
    else:
        return jsonify(student[id])

#render static file: storage
@server.route('/file/<path:namaFile>')
def myFile(namaFile):
    return send_from_directory('storage', namaFile)

#route untuk error
@server.errorhandler(404)
def notFound(error):
    return render_template('error.html')

if __name__ == '__main__':
    server.run(debug = True)