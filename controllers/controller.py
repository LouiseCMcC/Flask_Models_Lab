from app import app
from flask import render_template
from models.order_list import *

@app.route('/')
def index():
    return render_template('index.html', orders=orders)

@app.route('/order_list/<index_num>')
def display_one_order(index_num):
    return render_template('order.html', order=orders[int(index_num)])



