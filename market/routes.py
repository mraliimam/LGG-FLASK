from flask import render_template, redirect, url_for, flash, request
from market import app
from market import db
from market.static.func import GetOrder, PostOrder
#from market import db, Bcrypt
#from flask_login import login_user, logout_user, login_required
from datetime import date

@app.route('/')
@app.route('/home')
def home_page():
    return "PASS"

@app.route('/order', methods = ['GET','POST','PUT'])
def order_page():

    if request.method == 'GET':
        return GetOrder()
    
    elif request.method == 'POST':
        data = request.json()
        if PostOrder(data) != None:
            # return jsonify(data)
            return "Success"
        else: 
            return 'NULL'
    
    elif request.method == 'PUT':
        data = request.json()
        if PutOrder(data) != None:
            # return jsonify(data)
            return "Success"
        else:
            return 'NULL'
        