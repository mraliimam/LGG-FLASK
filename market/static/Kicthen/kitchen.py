from market import db
from market.models import Kitchen, Kitchen_Cart, Cart_Food, House, Cart

def addKitchen(cart):

    crt = Cart_Food.query.filter_by(Cart = cart)

    kName = House.query.filter_by(
                Name = Cart.query.filter_by(
                    Order_No = cart
                    ).first().House
                ).first().Kitchen

    for c in crt:

        if Kitchen_Cart.query.filter_by(Cart = cart, Food = c.Food).first():
            print('yes')
            continue
        else:
            k = Kitchen_Cart(
                Kitchen = kName,
                Food = c.Food,
                Cart = cart,
                Status = 'Kitchen'
            )

            db.session.add(k)            
            
            try:
                db.session.commit()
            except:
                db.session.rollback()
                print('Fail')
                return 'Fail'

            c.Status = 'Kitchen'
            db.session.add(c)
            
            try:
                db.session.commit()
            except:
                db.session.rollback()
                print('Fail')
                return 'Fail'

    crt2 = Cart.query.filter_by(Order_No = cart).first()
    crt2.Status = 'TO KITCHEN'
    db.session.add(crt2)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        print('Fail')
        return 'Fail'

    return 'Pass'

def getKitchen():

    kt = Kitchen_Cart.query.filter_by(Status = False)

    ds = db.engine.execute(f'''select k.kitchen, k.cart, f.Name, cf.Quantity, k.Status, k.food as fd from kitchen__cart k join Food f on f.id = k.food and k.Status not in ('DONE','DEL') join cart__food cf on cf.food = k.food;''')
    
    key = list(ds.keys())

    ds = list(ds)

    return ds,key

def postKitchen(act,record):

    db.engine.execute(f'''update kitchen__cart set Status = "{act}" 
                        where Cart = "{record[1]}" and Food = {record[5]} 
                        and Kitchen = "{record[0]}"''')
    db.session.commit()

    db.engine.execute(f'''update cart__food set Status = "{act}" where Cart = "{record[1]}" and Food = {record[5]} and Quantity = {record[3]}; ''')

    db.session.commit()

    return 'Pass'