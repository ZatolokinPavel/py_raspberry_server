#coding: utf-8
__author__ = 'Zatolokin Pavel'

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')    # берём настройки из файла config.py

from app import views
