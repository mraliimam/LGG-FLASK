from market.forms import OrderForm
from market.models import Tables, House_Food, Cart, Cart_Food, Member
from market import db

def readyOrder(house, cart, otype, oform):

    oform.table.choices = [i.Name for i in Tables.query.filter_by(House = house)]

    oform.otype.data = otype if otype == 'Takeaway' else 'Dine-IN'

    hse = House_Food.query.filter_by(House = house)

    foodTable = db.engine.execute(f'select f.id, f.Name, f.Sale_Price, f.Category from Food f join house__food hf on hf.category = f.category and hf.House = "{house}";')
    foodkeys = list(foodTable.keys())
    foodTable = list(foodTable)

    crt = Cart.query.filter_by(Order_No = cart).first()

    tflag = crt.tflag

    if tflag:
        oform.table.data = crt.Table
        oform.table.render_kw = {'readonly':True}
        oform.persons.data = crt.Persons
        oform.persons.render_kw = {'readonly':True}

    # Member.query.filter_by(
    #     id = Cart.query.filter_by(Order_No = cart).first().Member
    # ).first()

    mem = crt.Member

    return oform, hse, foodTable, foodkeys,tflag,mem


def addTable(form, cart):

    crt = Cart.query.filter_by(Order_No = cart).first()

    crt.Table = form['table']
    crt.Persons = form['persons']
    crt.tflag = True

    db.session.add(crt)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return 'Fail'
    
    tbl = Tables.query.filter_by(Name = form['table']).first()
    tbl.Status = True

    db.session.add(tbl)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return 'Fail'

    return 'Pass'

def addFood(form, cart, food):

    print(cart, food, form['Quantity'])
    crt = Cart_Food(
            Cart = str(cart),
            Food = int(food[0]),
            Quantity = int(form['Quantity']),
            Status = 'Cart'
        )

    db.session.add(crt)
    db.session.commit()

    return 'Pass'

def getCategory(house,category):
    
    hse = House_Food.query.filter_by(House = house, Category = category).first()
    return hse.id

def getOrders():

    results = Cart.query.filter(Cart.Status != 'DONE').all()
    return results, Cart.__table__.columns.keys()