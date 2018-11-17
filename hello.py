from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kot')
def kot():
    return '<h1> Koty sa smieszne </h1>'

@app.route('/user/<name>')
def users(name):
    return render_template('user.html', imie=name)

@app.route('/animals/kot')
def kotek():
    return '<img src="https://cutecats.com/wp-content/uploads/2015/03/ash.png">'

@app.route('/animals/pies')
def piesek():
    return '<img src="https://66.media.tumblr.com/7ebd5e238d283a7f426181f083085322/tumblr_pia8xk44Jz1rnbunpo1_500.jpg">'