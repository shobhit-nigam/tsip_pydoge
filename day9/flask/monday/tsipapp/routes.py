from tsipapp import app
from flask import render_template
from tsipapp.three import avengers

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', av=avengers)

@app.route('/index')
def index():
    user = {'name':'Toshiba'}
    return render_template('index.html', user=user, title='tsip')

@app.route('/tsip')
def tsip():
    user = {'name':'Toshiba'}
    return render_template('tsip.html', user=user, title='tttt', av=avengers)
