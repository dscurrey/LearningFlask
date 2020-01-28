from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'DCurrey'}
    entries = [
        {
            'author': {'username': 'Dave'},
            'body': 'Dave\'s Body Text'
        },
        {
            'author': {'username': 'NotDave'},
            'body': 'Some text also'
        }
    ]
    return render_template('index.html', title='Index', user=user, entries=entries)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Log In', form=form)
