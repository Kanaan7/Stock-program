import random
import logic

# verify Item code
while True:
    code=-1
    try:
        code = int(input(" insert Item code value (0-9999): "))
    except: pass
    if code >= 0 and code < 10000:
        break
    else: print("\nItem code must be an integer from 0-9999\n")
# verify Item name
while True:
    name=""
    name = input(" insert Item name: ")
    if (name.isalpha()) and len(name) > 2:
        break
    else: print("\nItem name must contain at least three characters and no numbers\n")
# verify price
while True:
    price=-1
    try:
        price = float(input(" insert Item price value: "))
    except: pass
    if price > 0:
        break
    else: print("\nItem price must be a real number greater than 0\n")
# verify manufacture cost
while True:
    manufacturecost=-1
    try:
        manufacturecost = float(input(" insert Item Manufacturing cost value: "))
    except: pass
    if manufacturecost > 0:
        break
    else:
        print("\nItem Manufacturing cost must be a real number greater than 0\n")
# verify Stcock level
while True:
    stock=-1
    try:
        stock = int(input(" insert Item Stcock level value: "))
    except: pass
    if stock > 0:
        break
    else: print("\nItem Stcock level must be an integer greater than 0\n")
# verify monthly units manufactured
while True:
    monthlymanufactured=-1
    try:
        monthlymanufactured = int(input(" insert Estimated monthly units manufactured value: "))
    except: pass
    if monthlymanufactured >= 0:
        break
    else: print("\nEstimated monthly units manufactured must be an integer greater than or equal to 0\n")
# Prints Item
print("\n Product Details\n") 
print("Item code: " + str(code)) 
print("Item name: " + str(name))
print("Item price: $" + str(price))
print("Item Manufacturing cost: $" + str(manufacturecost))
print("Item Stcock level: " + str(stock))
print("Estimated monthly units manufactured: " + str(monthlymanufactured))
# instantiates object
Product = logic.Item(code, name, price, manufacturecost, stock, monthlymanufactured)
# initializes simulation vars
monthlysold=0
netsold=0
profitorloss=0
# monthly sales simulation
print("\n MSS \n")
for i in range(1,13):
    Product.stock += Product.monthlymanufactured
    diff = random.randint(-10,10)
    monthlysold = Product.monthlymanufactured + diff
    Product.stock -= monthlysold
    netsold += monthlysold
    print("Month " + str(i) + ":")
    print("  Units manufactured:",str(Product.monthlymanufactured),"\n  Units sold:",str(monthlysold),"\n  Stock:",str(Product.stock))
# displays profit
profitorloss = (float(netsold)*float(Product.price))-(float(Product.monthlymanufactured) * float(Product.manufacturecost))
print("Your net profit or loss is: $" + str(profitorloss))