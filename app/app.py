from werkzeug.utils import redirect
from model.userModel import User
from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)
user = User()
URI = "http://localhost:5000/"

@app.route('/')
def index():
    result = user.fetch_all_user()
    return render_template('index.html', data=result)


@app.route('/add/')
def add_user_template():  
    return render_template('add_user.html')


@app.route('/add_user', methods=['POST', 'GET'])
def insert_user():
    data = request.form
    user.add_user(data)
    return redirect('http://localhost:5000')


@app.route('/delete/<id>')

def suppr(id):
    user.deleteById(id)

    return redirect(URI)

@app.route('/update_user/', methods=['POST', 'GET'])
def update_user():
    formData = request.form
    user.update(formData)
    return redirect(URI)

@app.route('/update/')
def formulaire_update():
    formData = request.args
    return render_template("update_user.html",data=formData)