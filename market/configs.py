from market import db
from market.models import Food


dic1 = {'Hot Beverage':li1}

li1 = ['Cappucino','Espresso','Cafe Latte','Cafe Solo','Americano','Doppio','Mix Tea','Green Tea','Black Tea']

li2 = [275,285,285,285,285,305,65,40,40]


for i in range(0,len(li1)):
    f = Food(id = i+1,Name = li1[i], Making_Price = 10, Sale_Price = int(li2[i]), Category = "Hot Beverage")
    db.session.add(f)
    db.session.commit()


li3 = ['Ali Imam', 'Saim Jamal', 'Ahmad', 'Tahir', 'Mateen']

li4 = ["Club House","Player's Lounge","19th Hole Cafe","BBQ Garden"]