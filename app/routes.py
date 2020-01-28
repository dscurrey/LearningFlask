from flask import render_template, flash, redirect
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Log In', form=form)
