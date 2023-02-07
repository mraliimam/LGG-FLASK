from market import db

from market.models import Cart


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

    crt = Cart(
        Order_No = form['Order_No'],
        House = form['House'],
        Member = form['Member'],
        OrderType = form['OrderType'],
        Status = 'ON HOLD'
    )

    db.session.add(crt)
    try:
        db.session.commit()
        return 'Pass'
    except:
        print("Error while creating a new Cart!!")
        db.session.rollback()
        return 'Fail'