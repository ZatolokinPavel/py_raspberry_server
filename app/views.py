#coding: utf-8
__author__ = 'Zatolokin Pavel'

from app import app
from flask import render_template, send_from_directory


@app.route('/py_back')
def index():
    return render_template("index.html", user=None)


# Раздача статики
@app.route('/py_back/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
