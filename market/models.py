from market import db
from market import bcrypt, login_manager
from flask_login import UserMixin
from datetime import datetime, date

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer(), primary_key=True)
#     username = db.Column(db.String(length=30), nullable=False, unique=True)
#     email = db.Column(db.String(length=50), nullable=False, unique=True)
#     password_hash = db.Column(db.String(length=60), nullable=False)
#     budget = db.Column(db.Integer(), nullable=False, default=1000)
#     items = db.relationship('Item', backref='owned_user', lazy=True)

#     @property
#     def password(self):
#         return self.password

#     @password.setter
#     def password(self, plain_text_password):
#         self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

#     def check_password_correction(self, attempted_password):
#         return bcrypt.check_password_hash(self.password_hash, attempted_password)

class House(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Name = db.Column(db.String(), nullable = False)
    Kitchen = db.Column(db.String(), db.ForeignKey('kitchen.Name'))
    kn = db.relationship('Kitchen')

class Kitchen(db.Model):
    Name = db.Column(db.String(), primary_key = True)

class Kitchen_Cart(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Kitchen = db.Column(db.String(), db.ForeignKey('kitchen.Name'))
    kn = db.relationship('Kitchen')
    Cart = db.Column(db.String(), db.ForeignKey('cart.Order_No'))
    ct = db.relationship('Cart')
    Food = db.Column(db.String(), db.ForeignKey('food.id'))
    fd = db.relationship('Food')
    Status = db.Column(db.String(), nullable = False)

class Tables(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Name = db.Column(db.String(), nullable = False)
    House = db.Column(db.String(), db.ForeignKey('house.Name'))
    hs = db.relationship('House')
    Status = db.Column(db.Boolean(), nullable = False, default = False)


class Member(db.Model):
    id = db.Column(db.String(), primary_key = True)
    Name = db.Column(db.String(), nullable = False)
    Type = db.Column(db.String(), nullable = False)
    Credit = db.Column(db.Integer(), nullable = False, default = 0)
    Phone = db.Column(db.String(), nullable = False)


class Food(db.Model):
    id = db.Column(db.Integer(), primary_key= True)
    Name = db.Column(db.String(), nullable = False)
    Making_Price = db.Column(db.Integer(), nullable = False)
    Sale_Price = db.Column(db.Integer(), nullable = False)
    Category = db.Column(db.String(), nullable = False)
    # House = db.Column(db.String(), db.ForeignKey('house.Name'))
    # sec = db.relationship('House')

class House_Food(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Category = db.Column(db.String(), db.ForeignKey('food.Category'))
    fd = db.relationship('Food')
    House = db.Column(db.String(), db.ForeignKey('house.Name'))
    hs = db.relationship('House')
    

class Cart(db.Model):
    Order_No = db.Column(db.String(), primary_key = True)
    Table = db.Column(db.String(), db.ForeignKey('tables.Name'))
    tbl = db.relationship('Tables')
    House = db.Column(db.String(), db.ForeignKey('house.Name'))
    hse = db.relationship('House')
    Persons = db.Column(db.Integer(), nullable = False, default = 1)
    OrderType = db.Column(db.String(), nullable = False)
    Member = db.Column(db.String(), db.ForeignKey('member.id'))
    mem = db.relationship('Member')
    Cash = db.Column(db.Boolean(), nullable = False, default = True)
    Status = db.Column(db.String(), nullable = False)
    Date = db.Column(db.Date(), nullable = False, default = date.today())
    Bill = db.Column(db.Integer(), nullable = False, default = 0)
    tflag = db.Column(db.Integer(), nullable = False, default = False)


class Cart_Food(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    Cart = db.Column(db.String(), db.ForeignKey('cart.Order_No'))
    cart_ref = db.relationship('Cart')
    Food = db.Column(db.String(), db.ForeignKey('food.id'))
    food_ref = db.relationship('Food')
    Quantity = db.Column(db.Integer(), nullable = False, default = 0)
    # Status = db.Column(db.Boolean, nullable = False, default = False)
    Status = db.Column(db.String(), nullable = False)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(), nullable = False)
    password = db.Column(db.String(), nullable = False)
    role = db.Column(db.String(), nullable = False)


# db.create_all()