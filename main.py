#Create a simple chatbot for a retail store that can answer customers' frequently asked questions about store hours, location, available products, and prices.
"""
FAQs:
store hours 
locations 
available products with prices- fruits, vegetables, juices 
"""
def options():
  return "\n****\n *for store hours enter 1 \n *for locations enter 2 \n *for available products with prices enter 3 \n *to talk to a representative enter 4 \n *to exit enter 5"
def store_hours():
  return "\n****\n Store hours:\n Mon thru Fri: 8am to 10 pm \n Sat thru Sun: 8am to 8pm"

def locations():
  return "\n****\n Our Locations: \n 875 Newcastle Ave. Orange, TX 77630, \n 531 Heather Drive Houston, TX 77062, \n 193 Railroad Drive Corpus Christi, TX 78413, \n 8956 Birch Hill Court Baytown, TX 77521"

def rep():
  return "\n****\n To talk to a representative please dial the number: 888-728-9732"
  
def fruits_and_price():
  return "\n****\n Fruits: \n Apples - $1.99/lbs \n Bananas - $2.40/lbs \n Oranges - $1.29/lbs \n Watermelons - $3.49/fruit \n Kiwis - $6.39/8oz. \n Avacados - $2.40/fruit \n Grapes - $2.46/lbs \n Cantalope - $2.99/fruit \n Bluberries - $3.57/8oz. \n Strawberries - $4.99/8oz. \n Pomegrantes - $2.10/fruit"

def veggie_and_price():
  return "\n***\n Vegetables: \n Celery - $2.88/8oz. \n Asparagus - $1.99/lbs \n Peas - $2.59/6oz. \n Kale - $3.49/lbs \n Beet - $3.45/lbs \n Broccoli - $2.99/9oz. \n Carrots - $2.23/8oz. \n Tomato - $1.98/lbs \n Potato - $1.99/lbs \n Corn - $0.98/bushel \n Onion - $1.00/lbs \n Bell Pepper - $0.98/pepper"

def juice_and_price():
  return "\n****\n Juices: \n Apple Juice - $3.45/56oz. \n Orange Juice - $2.49/56oz. \n Berry Juice - $3.69/46oz. \n Strawberry-Banana Juice - $2.89/56oz. \n Green Juice - $2.99/64oz. \n Tomato Juice - $2.43/56oz. \n Kale Juice - $3.34/56oz."



print("*****Welcome to the Grocery Store*****")
print("Hello, hope you are well.")
choice = input("Woud you like to view your options?(binary answer) ").lower()

while choice == 'yes':
  print(options())
  choice1 = float(input("\nEnter a number: "))
  if choice1 == 1:
    print(store_hours())
  if choice1 == 2:
    print(locations())
  if choice1 == 3:
    print("**\n for fruits enter 1 \n for vegetables enter 2 \n for juices enter 3")
    choice2 = float(input("\nEnter a number: "))
    if choice2 == 1:
      print(fruits_and_price())
    if choice2 == 2:
      print(veggie_and_price())
    if choice2 == 3:
      print(juice_and_price())
  if choice1 == 4:
    print(rep())
  if choice1 == 5:
    break

print("Thank you for visiting!!")