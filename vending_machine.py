Products = {
    "chips": {
        "code": {
            "doritos": 6,   # code is "doritos" and stock for 6
            "lays": 0,       
            "pringles": 5,   
        },
        "price": 125
    },
    "chocolate": {
        "code": {
            "cadbury": 10, 
            "mars": 8, 
            "lindt":0,    
        },
        "price": 150  
    },
    "drinks": {
        "code": {
            "coke": 5,    
            "sprite": 0, 
            "pepsi": 4,   
        },
        "price": 80  
    }
}

def display_stock():
    #products represents a dictionary that contains information about the products 
    for category, products in Products.items():
        print(f"\n***Stock for {category.capitalize()}:***")
        for product, stock in products["code"].items():
            print(f"      {product}: {stock}")
        print() 


def check_resources(order_products):
    for product, stock in order_products.items():
        if stock == 0:
            print(f"\n Sorry, {product.capitalize()} is out of stock. Please choose other items.")
            return False  
    return True 
 

def display_category_options(category):
    print(f"\n Available {category} options:")
    for code, stock in Products[category]["code"].items():
        item_cost = Products[category]["price"] 
        print(f"{code.capitalize()} ( Code: {code} / Price: {item_cost})")

        
def process_coins():
    print("\n Please insert coins.")
    total = 0
    
    while True:
        try:
            coins_five = int(input("How many 5rs coin?: "))
            coins_ten = int(input("How many 10rs coin?: "))
            coins_twenty = int(input("How many 20rs coin?: "))
            
            total = coins_five * 5 + coins_ten * 10 + coins_twenty * 20
            print("\n Total amount received:", total)
            break 
        except ValueError:
            print("\n Please enter only digits for the number of coins.")
    return total


profit=0
def is_payment_successful(money_received, product_price):
    if money_received >= product_price:
        global profit
        profit += product_price
        change = money_received - product_price
        print(f"\n You can collect your change: Rs{change}.")
        return True
    else:
        print("\n Sorry, the amount is not enough. Please collect your refunded money.")
        return False


def dispatch_product(category, product_choice):
    Products[category]["code"][product_choice] -= 1
    print(f"\n Here is your {product_choice.capitalize()}! Enjoy 😋")


#main program loop
is_running = True
while is_running:
    action = input("\nWhat would you like to do?\n1. Place an order\n2. Check stock\nEnter the number corresponding to your choice: ")

    if action == '1':
        choice = input("\n What would you like to have? (chips/chocolate/drinks): ")

        if choice == "off":
            is_running = False

        elif choice == "sales":
             print(f"\n Total sales = Rs{profit}")
            
        elif choice in Products:
            display_category_options(choice)
            
            while True:
                selected_item = input(f"\n Please enter {choice} code that you want to buy: ").strip().lower()
        
                if selected_item in Products[choice]["code"]:
                    
                    if check_resources({selected_item: Products[choice]["code"][selected_item]}):
                        payment = process_coins()
                        product_type = Products[choice]
                        if is_payment_successful(payment, product_type['price']):
                            dispatch_product(choice, selected_item)
                    break 
                else:
                    print("\n Product code is invalid. Please enter the correct product code.")          
        else:
            print("\n Invalid choice. Please choose among 'chips', 'chocolate' or 'drinks'.")

    elif action == '2':
        display_stock()

    else:
        print("\nInvalid choice. Please enter either '1' or '2'.")

    

