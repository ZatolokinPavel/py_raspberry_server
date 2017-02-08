__author__ = 'Zatolokin Pavel'

from app import app

@app.route('/py_back')
def index():
    return "Hello, World!"
