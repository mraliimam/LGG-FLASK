from flask import render_template, redirect, url_for, flash, request
from market import app
from market import db
from market.static.func import GetOrder, PostOrder
# from market.models import Customer, Tables, House_Food, House, Food
#from market import db, Bcrypt
#from flask_login import login_user, logout_user, login_required
from datetime import date
from market.static.Cart import cart

@app.route('/')
@app.route('/home')
def home_page():
    # return "PASS"
    return render_template('base.html')

@app.route('/order', methods = ['GET','POST'])
def order_page():

    if request.method == 'GET':
        # Pass id of members to check valid
        # cst = Customer.query.all()
        # cst_keys = Customer.__table__.columns.keys()

        # # # Pass the house names
        # # hse = House.query.all()
        # # hse_keys = House.__table__.columns.keys()

        # # Pass the food category names with respect to house
        # hseFood = House_Food.query.all()
        # hseFood_keys = House_Food.__table__.columns.keys()

        # # Pass the food Items
        # fd = Food.query.filter_by(Category = "This")
        # fd_keys = Food.__table__.columns.keys()

        # Constantly updating temp cart Pass the cart status and values

        ids = cart.genId()

        return render_template('order.html', ids = ids)

    if request.method == 'POST':

        if cart.newCart(request.form) == 'Fail':
            return redirect(url_for('order_page'))
        else:
            return redirect(url_for('order_page'))

@app.route('/orderPage', methods = ['GET', 'POST'])
def order_details():

    if request.method == 'GET':

        return render_template('orderDetails.html')

    if request.method == 'POST':

        pass