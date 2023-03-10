from market import db

from market.models import Cart, Cart_Food


def genId():

    for i in Cart.query.all():
        pass
        
    try:
        m = i.Order_No
        m = m[1:]
        m = int(m)
        m += 1
        m = 'c'+str(m)
        return m
    except:
        m = 'c320001'
        return m

def newCart(form):

    s = 'Takeaway' if form['OrderType'] == 'Takeaway' else 'Table'
    crt = Cart(
        Order_No = form['Order_No'],
        House = form['House'],
        Member = form['Member'],
        OrderType = form['OrderType'],
        Table = s,
        Status = 'ON HOLD'
    )

    db.session.add(crt)
    # try:
    #     db.session.commit()
    #     return 'Pass'
    # except:
    #     print("Error while creating a new Cart!!")
    #     db.session.rollback()
    #     return 'Fail'
    db.session.commit()
    return 'Pass'

def getCart(cart):

    results = Cart_Food.query.filter_by(Cart = cart)

    # results = Cart.query.filter(Cart.Status != 'DONE').all()

    results = db.engine.execute(f'select f.Name, f.Category, cf.Quantity, cf.Status from Food f join cart__food cf on cf.food = f.id and cf.cart = "{cart}";')

    key = list(results.keys())
    results = list(results)

    return results, key