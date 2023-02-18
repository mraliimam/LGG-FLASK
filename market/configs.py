from market import db
from market.models import Food, Tables, House_Food

# dic1 = {'Hot Beverage':li1}

# li1 = ['Cappucino','Espresso','Cafe Latte','Cafe Solo','Americano','Doppio','Mix Tea','Green Tea','Black Tea']

# li2 = [275,285,285,285,285,305,65,40,40]

# for i in range(0,len(li1)):
#     f = Food(id = i+1,Name = li1[i], Making_Price = 10, Sale_Price = int(li2[i]), Category = "Hot Beverage")
#     db.session.add(f)
#     db.session.commit()


# li3 = ['Ali Imam', 'Saim Jamal', 'Ahmad', 'Tahir', 'Mateen']

# li4 = ["Club House","Player's Lounge","19th Hole Cafe","BBQ Garden"]

# #========================================

# # House

# li = ["Club House", "Player's Lounge", "Front Lawn", "19th Hole Cafe", "BBQ Garden", "Lack Deck"]

# hse = House(Name = li[0], Kitchen = li[0])
# db.session.add(hse)
# db.session.commit()

# Tables

li = {"Club House":14, "Player's Lounge":12, "Front Lawn":20, "19th Hole Cafe":15, "BBQ Garden":14, "Lack Deck":10}

# for i in li:
#     tbl = Tables(Name = "Takeaway", House = i)
#     db.session.add(tbl)
#     db.session.commit()

for i in li:
    l = 1
    for j in range(li[i]):
        if i[0] == '1':
            k = 'H'
        else:
            k = i[0]
        tbl = Tables(Name = k+str(l), House = i)
        db.session.add(tbl)
        db.session.commit()
        l+=1

#=============================================

hb1 = ['Cappucino','Espresso','Cafe Latte','Cafe Solo','Americano','Doppio','Mix Tea','Green Tea','Black Tea']
hb2 = [275,285,285,285,285,305,65,40,40]

cc1 = ['Strawberry Smoothie', 'Lychee Smoothie', 'Mint Margarita', 'Pina Colada', 'Oreo Strawberry Kiss', 'Cold Coffee', 'Fresh Seasonal Juices', 'Mineral Water (S)', 'Mineral Water (L)', 'Soft Drink', 'Fresh Lemon 7up']
cc2 = [250,250,185,295,295,295,180,45,80,65,80]

sa1 = ['Chocolate Molten Lava Cake', 'Tiramisu', 'Bread and Butter Pudding', 'Walnut Tart']
sa2 = [510,510,450,450]

b1 = ['The Fireman Burger', 'The Pakistani Burger', 'Club Special Burger', 'Chicken Mushroom Cheese Burger', 'Butter Milk Burger']
b2 = [595,570,660,545,665]

sw1 = ['Grilled Chicken Sandwich', 'The Club House Sandwiches', 'BBQ Chicken Sandwich', 'Roast Beef Sandwich', 'Mexican Quesadilla', 'Burritos']
sw2 = [490,635,490,575,575,575]

st1 = ['Chicken Steak', 'Beef Steak (Fillet Mignon)', 'Choice of Potatoes & Sauce']
st2 = [890,1095,500]

p1 = ['Fettuccine Alfredo', 'Penne Arrabiata', 'Spagheti Bolognese']
p2 = [570,570,570]

py1 = ['Stuffed Breast of Chicken', 'Grilled Chicken Maxican', 'Chicken Parmigiana', 'Katsu Chicken', 'Grilled Chicken (Tarragon Sauce)', 'Chiecken Sashlick', 'Barbecue American Chicken']
py2 = [775,755,875,715,775,775,775]

as1 = ['Fish N Chips', 'Meuniere Fish Almondine', "Grilled Fillet of Fish (Mexican)", 'Fried Jumbo Prawns']
as2 = [1125,1125,1125,1275]

sk1 = ['Muligatawny Soup', 'Cream of Chicken Soup', 'Roasted Tomato Soup', 'Soup of the day']
sk2 = [265,265,265,265]

sd1 = ['Caesar Salad', 'Greek Salad', 'Hummus Salad', 'Waikiki Salad']
sd2 = [375,375,325,375]

swt1 = ['Dynamite Chicken Tenders', 'Buffalo Chicken Wings', 'Fish Fingers', 'Fried Mozarella Sticks']
swt2 = [540,490,995,745]

bfs1 = ['Omelette Fiesta', 'American Breakfast', 'Classic Eggs Benedict', 'Club Special Breakfast', 'Our Tradition', 'Chicken Waffles', 'Finest French Toast']
bfs2 = [485,560,540,620,450,560,495]

dic1 = {'Hot Beverage':hb1, 'Cold Corner':cc1, 'Sweet Affairs':sa1, 'Burgers': b1, 'Sandwiches & Wraps': sa1, 'Steaks': st1, 'Pastas': p1, 'Poultry':py1, 'From The Arabian Sea': as1, 'From The Soup Kettle': sk1, 'Salads': sd1, 'To Start With': swt1, 'Breakfast': bfs1}
priceList = [hb2,cc2,sa2,b2,sw2,st2,p2,py2,as2,sk2,sd2,swt2,bfs2]

for i,j in zip(dic1.keys(), priceList):
        for k,l in zip(dic1[i],j):
            f = Food(Name = k, Making_Price = 10, Sale_Price = l, Category = i)
            db.session.add(f)
            try:
                db.session.commit()
            except:
                print(k,l,i)
                db.session.rollback()

#=================================================

ds1 = ['Thooti', 'Bread Pudding', 'Tiramisu', 'Gajar Halwa (Seasonal)', 'Fresh Jalaibi']
ds2 = [130,130,160,140,120]

sf1 = ['Soft Drink 500ml', 'Soft Drink 1.5 Ltr', 'Fresh Lime', 'Mineral Water 500ml', 'Mineral Water 1.5 Ltr']
sf2 = [75,130,70,80,45]

sap1 = ['Healthy Green Salad', 'Russian Salad', 'Kachumar Salad', 'Fattoush Salad']
sap2 = [125,220,220,290]

cg1 = ['Charcoal Grilled Fish Tikka', 'Peshawari Mutton Tikka', 'Chicken Mutton Tikka', 'Chicken Tikka', 'Chicken Afghani Tikka', 'Grilled Chicken Boti', 'Reshmi Seekh Kabab', 'Beef Khoya Kabab', 'Mughlai Kabab', 'Behari Kabab', 'Grilled Lamb Chops', 'Chicken Sajji', 'Chicken Chargha', 'Grilled Chicken Moroccan', 'Barbecue Delight', 'Achari Lovers']
cg2 = [910,1010,495,300,570,430,440,680,725,540,955,1090,955,610,600,520]

fok1 = ['Chicken Madarasi Handi', 'Chicken Boneless Handi', 'Chicken Jalferazi', 'Chicken Ginger Masala', 'Chicken Chop Masala', 'Chicken Karahi', 'Dal Mash', 'Mutton Karahi', 'Lamb Brain Masala', 'Mutton Chops Masala', 'Mutton Stew in Matka', 'Fish Malwari', 'Palak Paneer', 'Mix Achari Vegetable', 'Club Special Biryani']
fok2 = [1005,1025,1030,1030,960,960,345,2225,730,1060,2210,1700,520,440,395]

pml1 = ['Barbecue Platter', 'Seafood Platter']
pml2 = [995,1240]

co1 = ['Kalwanji Nan', 'Roghni Nan', 'Tandoori Roti', 'Khameeri Roti']
co2 = [50,50,50,15,40]

dic2 = {'Dessert':ds1,'Beverages':sf1, 'Salad & Appetizers':sap1, 'Charcoal Grill':cg1,'From Our Kitchens':fok1, 'Platter Meal':pml1, 'Clay Oven':co1}
priceLists = [ds2, sf2, sap2, cg2, fok2, pml2, co2]

for i,j in zip(dic2.keys(), priceLists):
        for k,l in zip(dic2[i],j):
            f = Food(Name = k, Making_Price = 10, Sale_Price = l, Category = i)
            db.session.add(f)
            try:
                db.session.commit()
            except:
                print(k,l,i)
                db.session.rollback()

#====================================================

sp1 = ['Cream of Chicken Soup', 'Chicken Corn Soup', 'Vegetable Clear Soup', 'Hot & Sour Soup']
sp2 = [150,130,130,130]

apt1 = ['Chicken Nuggets', 'Fish Cracker']
apt2 = [330,120]

sd1 = ['Russian Salad', 'Katchumer Salad', 'Fresh Green Salad']
sd2 = [325,220,180]

sb1 = ['Chicken Sandwich', 'Club Special Sandwich', 'Chicken Burger', 'Chicken Cheeze Burger', 'Fried Chicken Breast Burger', 'Fish Burger']
sb2 = [225,330,350,360,360,450]

sf1 = ['Fried Fish', 'Fish Finger']
sf2 = [790,790]

ot1 = ['Chicken Karahi Half', 'Chicken Karahi Full', 'Chicken B/L Handi Half', 'Chicken B/L Handi Full', 'Chicken Madrasi Handi', 'Chicken Ginger Masala', 'Mutton Karahi Half', 'Mutton Karahi Full', 'Mutton Chops Masala', 'Lamb Brain Masala', 'Dall Mash Handi']
ot2 = [550,1030,550,1025,1005,1025,1150,2295,1070,860,400]

ps1 = ['Chicken Manchurian', 'Chicken Almond', 'Chicken Stroganoff', 'Chicken with Mixed Vegetable', 'Chicken Szechuan', 'Chicken with Garlic Sauce', 'Chicken Chili Dry', 'Chicken Chowmein', 'Chicken with Cashewnut', 'Sweet & Sour Chicken', 'Chicken Shashlik', 'Fish with Garlic Sauce']
ps2 = [530,560,500,495,525,535,495,395,530,495,530,725]

rc1 = ['Chicken Fried Rice', 'Egg Fried Rice', 'Chicken Masala Rice', 'Garlic Fried Rice']
rc2 = [380,400,440,400]

sc1 = ['Cream Caramel', 'Shahi Kheer', 'Ice Cream']
sc2 = [130,130,130]

bg1 = ['Soft Drinks (500ml)', 'Diet 7up', 'Fresh Lime 7up', 'Mineral Water (Large)', 'Mineral Water (Small)', 'Soft Drink 1500ml']
bg2 = [70,70,80,80,45,130]

dic3 = {'Soups':sp1, 'Appetizer': apt1, 'Salad':sd1, 'Sandwich & Burgers': sb1, 'Sea Food': sf1, 'Our Tradition':ot1, 'Platters': ps1, 'Rice':rc1, 'Sweet Corner': sc1, 'Beverage': bg1}
priceList = [sp2, apt2, sd2, sb2, sf2, ot2, ps2, rc2, sc2, bg2]

for i,j in zip(dic3.keys(), priceList):
        for k,l in zip(dic3[i],j):
            f = Food(Name = k, Making_Price = 10, Sale_Price = l, Category = i)
            db.session.add(f)
            try:
                db.session.commit()
            except:
                print(k,l,i)
                db.session.rollback()

for i in dic1.keys():
    hs = House_Food(Category = i, House = '19th Hole Cafe')
    db.session.add(hs)
    try:
        db.session.commit()
    except:
        db.session.rollback()


for i in dic3.keys():
    hs = House_Food(Category = i, House = 'Club House')
    db.session.add(hs)
    try:
        db.session.commit()
    except:
        db.session.rollback()

print("Done")



#======================================================================

kiList = ['Club House', "Player's Lounge", '19th Hole Cafe', 'BBQ Garden']

for k in kiList:
    ki = Kitchen(
        Name = k
    )
    db.session.add(ki)
    db.session.commit()


for k in kiList:
    hs = House(
        Name = k,
        Kitchen = k
    )
    db.session.add(hs)
    db.session.commit()