coffee= """
    ( (
     ) )
  ........
  |      |]
  \\      /
   `----'
"""
waving_hand_bye = """
  o/
 /|   Bye!
/ >
"""

closed_message = """
      _______
    /        \\
   |  WE ARE  |
   |  CLOSED  |
   |   NOW    |
    \\_______/  
      |     |
      |     |
     /|     |\\
    / |     | \\
   /  |     |  \\
  /   |_____|   \\
      /     \\
     /       \\
"""
coffee_vending_machine = """
  ___________________________
 |      ____   Cafe Coffee   |
 |     | __ |      Day       |
 |     |____|                |
 |      ____                 |
 |     |    |   Insert       |
 |     |____|   Coins        |
 |      ____     |           |
 |     |    |    |           |
 |     |____|    |           |
 |      ____     |           |
 |     |    |    V           |
 |     |____|  _______       |
 |      ____  |  ___  |      |
 |     |    | | |   | |      |
 |     |____| | |___| |      |
 |      ____  |       |      |
 |     |    | |_______|      |
 |     |____|                |
 |      ____   Espresso $1.5 |
 |     |    |   Latte    $2.5|
 |     |____|   Cappuccino $3|
 |___________________________|
     ||        ||
     ||        ||
     ||________||
"""

MENU = {
  "espresso": {
      "ingredients": {
          "water": 50,
          "coffee": 18,
      },
      "cost": 1.5,
  },
  "latte": {
      "ingredients": {
          "water": 200,
          "milk": 150,
          "coffee": 24,
      },
      "cost": 2.5,
  },
  "cappuccino": {
      "ingredients": {
          "water": 250,
          "milk": 100,
          "coffee": 24,
      },
      "cost": 3.0,
  }
}

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
  "Money": 0.0

}

end=False

def start ():

 if user_choice=="report":
      report()
 if user_choice=="espresso" or user_choice=="latte" or user_choice=="cappuccino":
            check=check_requirements(user_choice)
            if check==True :
                payment=process_coins (user_choice)
                if payment==True :
                    make_coffee(user_choice)
            else :
                print("Sorry , we do not have enough ingredients right now \n")



def report():
    Milk=resources["milk"]
    Water=resources["water"]
    Coffee=resources["coffee"]
    Money=resources["Money"]
    print(f" Milk : {Milk} \n Water : {Water} \n Coffee : {Coffee} \n Money : {Money}")

def check_requirements (a):
    check1=False
    if a=="espresso" and resources["water"] > MENU["espresso"]["ingredients"]["water"] and resources["coffee"] > MENU["espresso"]["ingredients"]["coffee"]:
        check1=True
    if a!="espresso":
       if resources["water"] > MENU[a]["ingredients"]["water"] and resources["coffee"] > MENU[a]["ingredients"]["coffee"] and resources["milk"] > MENU[a]["ingredients"]["milk"] :
         check1 = True
       else:
         check1=False
    return check1

def process_coins(a):
    quarters=int(input("How many quarters would you like to enter ?"))
    dimes=int(input("How many dimes would you like to enter ?"))
    nickles=int(input("How many nickles would you like to enter ?"))
    pennies=int(input("How many pennies would you like to enter ?"))
    global amount_entered
    amount_entered = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    if amount_entered==MENU[a]["cost"] :
        print("Payment successful , Your coffee is getting ready ")
        resources["Money"]+=amount_entered
        return True
    elif amount_entered>MENU[a]["cost"] :
        print("Payment successful ")
        change =-MENU[a]["cost"]+amount_entered
        print(f"Change : ${change}")
        resources["Money"]+=(amount_entered-change)
        return True
    elif amount_entered<MENU[a]["cost"] :
        amt=MENU[a]["cost"]
        print(f"Payment unsuccessful , Your bill is ${amt} ")
        print("Money refunded")
        return False

def make_coffee(a):
    if a=="espresso" :
        resources["water"]-=MENU["espresso"]["ingredients"]["water"]
        resources["coffee"]-=MENU["espresso"]["ingredients"]["coffee"]
    else:
        resources["water"]-=MENU[a]["ingredients"]["water"]
        resources["coffee"]-=MENU[a]["ingredients"]["coffee"]
        resources["milk"]-=MENU[a]["ingredients"]["milk"]
    print ("Your coffee is ready !!! ☕ \n ")
    print(f" {coffee}\n")

def off() :
 print("Machine closed ")
 print(closed_message)
 return True


while not end :
    print(coffee_vending_machine)
    user_choice=(input("What would you like to have - espresso , latte , cappuccino? \n")).lower()
    if user_choice=="off" :
        end=off()
        break
    start()
    purchase_choice=(input("Do you want to purchase more - yes or no ? \n")).lower()
    if purchase_choice=="yes":
        end=False
    else:
        print("BYE BYE !! HAVE A GOOD DAY ")
        print(waving_hand_bye)
        end =True
        break









