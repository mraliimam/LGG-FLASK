from market import db
import json
from market import models

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

def dbs2dict(rows):
    
    dic = {}
    for i in rows:
        if(i[0] in dic.keys()):
            dic[i[0]].append(i[1])
        else:
            dic[i[0]] = []
            dic[i[0]].append(i[1])
    return dic

def GetOrder(ids):

    #=========== Retreive List of Members ====================================================
    rows = db.engine.execute('select id from customer;')
    rows = rows.fetchall()
    result = {"id":[]}
    for i in rows:
        result['id'].append(i[0])
    
    #============ Food List Category Wise Response ===========================================
    rows1 = db.engine.execute('select Name, Sale_Price, Category from food order by Category;')
    rows1 = rows1.fetchall()
    dic1 = {}
    for i in rows1:
        if(i[2] in dic1.keys()):
            dic1[i[2]].append([i[0],i[1]])
        else:
            dic1[i[2]] = []
            dic1[i[2]].append([i[0],i[1]])
    result1 = dic1

    #============ List of Table order by House Sections ========================================
    rows2 = db.engine.execute('select Name, House from Tables;')
    rows2 = rows2.fetchall()
    result2 = dbs2dict(rows2)
    
    #============ List of Food Category according to House Section =============================
    rows3 = db.engine.execute('''select h.Name, f.Category from Food f left join house__food hf on 
                                hf.category = f.category join house h on h.id = hf.house;''')
    rows3 = rows3.fetchall()
    result3 = dbs2dict(rows3)

    #============ List of Cart Items and Quantity ==============================================
    if(ids == None):
        result4 = {}
    
    else:
        rows4 = db.engine.execute('''select  ''')
        pass

    #=========== Combining the responses into a list ===========================================
    # last = [result,result1,result2, result3]
    last = {"Members":result,"Food":result1, "House Tables":result2, "House Categories": result3}

    #========== Converting combined list to JSON Response =====================================
    res = json.dumps(last)

    return res

def PostOrder(forms):

    data = json.loads(forms)

    if models.Customer.query.filter_by(id = data['Cust_id']).first() != None:

        cash = 1 if data['Status'] == 'Cash' else 0

        crt = models.Cart(
            Order_No = data['Cart_id'],
            Table = data['Table_No'],
            Persons = data['Persons'],
            Member = data['Cust_id'],
            Cash = cash,
            Status = data['Status'],
            Bill = data['Bill']
        )
        db.session.add(cst)
        try:
            db.session.commit()
        except:
            print("Error Occured")
            db.session.rollback()
            return "Fail"

        for ids,quan in data['Food']['id'],data['Food']['Quantity']:

            crtf = models.Cart_Food(
                Cart = data['Cart_id'],
                Food = ids,
                Quantity = quan
            )

            db.session.add(crtf)
            try:
                db.session.commit()
            except:
                print("Error Occured")
                db.session.rollback()
                return "Fail"

    else:
        return "pass"

    
def PutOrder():

    data = json.loads(forms)

    crt = models.Cart.query.filter_by(Order_No = data['Cart_id']).first()

    if crt != None:

        for ids,quan in data['Food']['id'],data['Food']['Quantity']:

            fdd = model.Cart_Food.query.filter_by(Food = ids).first()

            if fdd == None:
                crtf = models.Cart_Food(
                    Cart = data['Cart_id'],
                    Food = ids,
                    Quantity = quan
                )

                db.session.add(crtf)
                try:
                    db.session.commit()
                except:
                    print("Error Occured")
                    db.session.rollback()
                    return "Fail"

        crt.Cash = data['Status']
        crt.Bill = data['Bill']

        db.session.add(crt)
        try:
            db.session.commit()
        except:
            print("Error Occured")
            db.session.rollback()
            return "Fail"

    return 'pass'