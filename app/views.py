#coding: utf-8
__author__ = 'Zatolokin Pavel'

from app import app
from flask import render_template, send_from_directory
from flask import redirect
from forms import LoginForm

base_url = app.config.get('BASE_URL', '')           # начало для всех uri приложения


@app.route(base_url + '/')
@app.route(base_url + '')
def index():
    return render_template("index.html",
                           base_url=base_url,
                           user=None)


@app.route(base_url + '/power')
def power_page():
    return render_template("power.html",
                           base_url=base_url,
                           user=None,
                           is_power_on=False)


@app.route(base_url + '/login', methods=['GET', 'POST'])
def login_form():
    form = LoginForm()
    if form.validate_on_submit():                   # если форма заполнена и провалидировалась...
        return redirect(base_url)
    return render_template('login.html',
                           base_url=base_url,
                           user=None,
                           form=form)


# Раздача статики
@app.route(base_url + '/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
