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
    # return "PASS"
    return render_template('base.html')

@app.route('/order', methods = ['GET','POST','PUT'])
def order_page():

    if request.method == 'GET':
        # Pass id of members to check valid
        cst = Customer.query.all()
        cst_keys = Customer.__table__.columns.keys()

        # # Pass the house names
        # hse = House.query.all()
        # hse_keys = House.__table__.columns.keys()

        # Pass the food category names with respect to house
        hseFood = House_Food.query.all()
        hseFood_keys = House_Food.__table__.columns.keys()

        # Pass the food Items
        fd = Food.query.filter_by(Category = "This")
        fd_keys = Food.__table__.columns.keys()

        # Constantly updating temp cart Pass the cart status and values
        
    pass