#initializing Inventory
InitialInventory={
    "Water":100,
    "Milk":50,
    "Coffee":76,
    "Money":2.5
}
#initializing Inventory
#inventory = InitialInventory

#MENU ITEMS BY PRICE AND QUANTITY
latte={"Water":250,"Milk":55,"Coffee":77,"Price":1.5}
espresso={"Water":50,"Milk":0,"Coffee":9,"Price":1.5}
cappuccino={"Water":70,"Milk":10,"Coffee":20,"Price":1.0}

def report():
    print("---CURRENT RESOURCES---")
    print("Water :",str(inventory["Water"])+"ml")
    print("Milk :",str(inventory["Milk"])+"ml")
    print("Coffee :",str(inventory["Coffee"])+"g")
    print("Money :","$"+str(inventory["Money"]))

def coinProgram():
    print("--Insert Coins--")
    quarters=int(input("Insert Quarters : "))
    dimes=int(input("Insert Dimes : "))
    nickeles =int(input("Insert Nickles : "))
    pennies=int(input("Insert Pennies : "))
    calc = quarters*.25 + dimes*.10 +nickeles*.05 +pennies*.01
    return round(calc,2)

def checkResource(item):
    if item["Water"]> inventory["Water"]:
        print("Sorry there is NOT enough Water.")
        if item["Milk"]> inventory["Milk"]:
            print("Sorry there is NOT enough Milk.")
            if item["Coffee"]> inventory["Coffee"]:
                print("Sorry there is NOT enough Coffee.")
    else:
        transaction(item)
    

def transaction(item):
    insertedCoins=coinProgram()
    price=item["Price"]
    #print(insertedCoins,price)
    if insertedCoins < price:
        print("Sorry that's not enough money. Still need $"+str(round(price-insertedCoins,2)),"more. Money refunded.")
    elif insertedCoins >= price:
        inventory["Money"]=inventory["Money"]+price
        makeCoffee(item)
        if insertedCoins > price:
            print("Here is $"+str(round(insertedCoins-price,2)),"in change.")

def makeCoffee(item):
   inventory["Water"]=inventory["Water"]-item["Water"]
   inventory["Milk"]=inventory["Milk"]- item["Milk"]
   inventory["Coffee"]=inventory["Coffee"] - item["Coffee"]
   print("Here is your",str(prompt)+". Enjoy!")


while True:
    print("-----COFFEE_PROGRAM-----")
    inventory = InitialInventory

    prompt=input("What would you like? (espresso/latte/cappuccino) :")
    
    if prompt == "off":
        print("---Turning off---")
        break

    elif prompt=="report":
        report()
    
    elif prompt=="espresso":
        checkResource(espresso)
    
    elif prompt=="latte":
         checkResource(latte)

    elif prompt=="cappuccino":
        checkResource(cappuccino)
    else:
        print("Sorry.Something went wrong.Please Try Again!")
        print("off to trun off and report for report")
    
