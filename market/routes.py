from flask import render_template, redirect, url_for, flash, request
from market import app
from market import db
# from market.static.func import GetOrder, PostOrder
from market.models import Tables, House_Food
from market.forms import OrderForm
from market.static.Order import order
from market.static.Kicthen import kitchen
from market.static.Member import member
from market.static.func import con1
# from market.models import Customer, Tables, House_Food, House, Food
#from market import db, Bcrypt
#from flask_login import login_user, logout_user, login_required
from datetime import date
from market.static.Cart import cart

@app.route('/')
@app.route('/home')
def home_page():
    
    return render_template('base.html')

@app.route('/order', methods = ['GET','POST'])
def order_page():

    if request.method == 'GET':

        ids = cart.genId()

        return render_template('order.html', ids = ids)

    if request.method == 'POST':

        mm = member.validateMember(request.form['Member'])
        if mm == 'Pass':
            if cart.newCart(request.form) == 'Fail':
                flash('Error Occured while Creating the new Cart', category='danger')
                return redirect(url_for('order_page'))
            else:
                return redirect(url_for('order_details', cart = request.form['Order_No'], house = request.form['House'], ordertype = request.form['OrderType']))
        elif mm == 'Fail':
            flash('Membership ID is not Valid!!', category='danger')
            return redirect(url_for('order_page'))

@app.route('/orderPage', methods = ['GET', 'POST'])
def order_details():

    oform = OrderForm()
    house = request.args.get(key = 'house')
    cart = request.args.get(key = 'cart')
    otype = request.args.get(key = 'ordertype')
    cat = request.args.get(key = 'cat')

    if request.method == 'GET':

        oform,hse,foodTable,foodkeys,tflag,mem = order.readyOrder(house, cart, otype, oform)

        return render_template('orderDetails.html', cart = cart, house = hse, oform = oform, 
                                foodTable = foodTable, foodkeys = foodkeys, cat = cat, tflag = tflag, mem = mem)

    if request.method == 'POST':

        if 'table' in request.form.keys():
            
            order.addTable(request.form, cart)
            oform.persons.render_kw = {'disabled':True}
            oform.table.render_kw = {'disabled':True}
            flash('Table Allocated Successfully!!', category = 'success')
            
        
        elif 'food' in request.form.keys():
            
            form = request.form.copy()
            food = con1(form['food'])
            order.addFood(request.form, cart,food)
            cat = order.getCategory(house,food[3])
            flash('Food Added Successfully!!', category = 'success')

        return redirect(url_for('order_details', cart = cart, house = house, ordertype = otype, cat = cat))

@app.route('/pendingOrders', methods = ['GET', 'POST'])
def pending_page():

    if request.method == 'GET':
        crt,key =  order.getOrders()
        return render_template('pendingOrder.html', cart = crt, key = key)


@app.route('/cart', methods = ['GET', 'POST'])
def cart_page():

    crtID = request.args.get(key = 'cart')

    if request.method == 'GET':

        crt,key = cart.getCart(crtID)
        return render_template('cart.html', cart = crt, key = key, cartID = crtID)

    if request.method == 'POST':

        form = request.form.copy()

        # record = con1(form['record'])

        # for i in form.keys():
        #     print(form[i])
        
        if 'cart' in form.keys():

            record = con1(form['record'])
            db.engine.execute(f'''delete from cart__food where 
                                  food = (select f.id from food f 
                                  where Name = '{record[0]}') and cart = '{crtID}';''')
            db.engine.execute(f'''delete from kitchen__cart where
                                  food = (select f.id from food f
                                  where Name = '{record[0]}') and cart = '{crtID}' ''')

            db.session.commit()
            
            return redirect(url_for('cart_page', cart = crtID))

        elif 'Kitchen' in form.keys():

            cartID = form['Kitchen']

            kitchen.addKitchen(cartID)

            return redirect(url_for('pending_page'))

        return redirect(url_for('cart_page', cart = crtID))

@app.route('/kitchen', methods = ['GET','POST'])
def kitchen_page():

    if request.method == 'GET':

        crt,key = kitchen.getKitchen()
        return render_template('kitchen.html', cart = crt, key = key)

    if request.method == 'POST':

        act = request.form.get(key = 'action')
        record = request.form.get(key = 'order')

        # db.engine.execute(f'''update kitchen__cart set Status = "{act}" 
        #                     where Cart = "{record[1]}" and Food = {record[2]} 
        #                     and Kitchen = "{record[1]}"''')

        record = con1(record)
        # for i in record:
        #     print(i)
        # print(act)
        kitchen.postKitchen(act,record)

        return redirect(url_for('kitchen_page'))