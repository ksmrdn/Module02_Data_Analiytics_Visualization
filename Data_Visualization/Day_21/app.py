from flask import Flask, jsonify, send_from_directory, render_template, abort, redirect, request
app = Flask(__name__)

#Home route
@app.route('/')
def home():
    return render_template('home.html')

student = [{"id":0,"nama":"Ksmrdn","usia":21,"kota":"Surabaya"},
       {"id":1,"nama":"Ksmrdna","usia":22,"kota":"Surabaya"},
       {"id":2,"nama":"Ksmrdni","usia":23,"kota":"Surabaya"},
       {"id":3,"nama":"Ksmrdnu","usia":24,"kota":"Surabaya"}]

#route response json
@app.route('/member')
def std():
    return jsonify(student)

@app.route('/home')
def beranda():
    return redirect('/')

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == 'GET':
        return 'GET GET GET'
    elif request.method == 'POST':
        body = request.json
        print(body)
        return jsonify({
            'status': 'Data Sukses Terkirim',
            'nama': body['name'],
            'kota' : body['city'],
            'usia' : body['age']
        })
    else:
        return 'Neither GET nor PUSH'

if __name__ == '__main__':
    app.run(debug=True, port=1928)