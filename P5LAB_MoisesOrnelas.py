#Moises Ornelas
#4-10-2024
#P5LAB
#user determined functions

#define function

def disperse_change(change):
    print(f"Change owed: {change}")    
    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed
    #integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed

    if num_dollars > 0:
            print(num_dollars,  end=" ")
            if num_dollars == 1:
                print("Dollar")
            else:
                print("Dollars")
                
    if num_quarters > 0:
            print(num_quarters,  end=" ")
            if num_quarters == 1:
                print("Quarter")
            else:
                print("Quarters")

    if num_dimes > 0:
            print(num_dimes,  end=" ")
            if num_dimes == 1:
                print("Dime")
            else:
                print("Dimes")

    if num_nickles > 0:
            print(num_nickles,  end=" ")
            if num_nickles == 1:
                print("Nickle")
            else:
                print("Nickles")

    if num_pennies > 0:
            print(num_pennies,  end=" ")
            if num_pennies == 1:
                print("Penny")
            else:
                print("Pennies")


def show_available_items(dictionary):
    print(f"{'Grocery Item':<25}{'Price'}")
    print("---------------------------------")
    for key, value in dictionary.items():
        print(f"{key:<25}{value:.2f}")
    print("----------------------------------")     
        
def add_items(dictionary):
    cart = []
    items = input("Enter an item to add to the cart or type 'end' to stop adding items: ")
    while items != "end":
        if items in dictionary.keys():
            cart.append(items)
        else:
            print(f"{items} is not in stock")
            
        items = input("Enter an item to add to the cart or type 'end' to stop adding items: ")    
    return cart
            
def get_total(cart, dictionary):
    total = 0
    for items in cart:
        total += dictionary[items]
    return total    

#main logic starts here
#call function
def main():
    #create dictionary with items and prices
    items = {"apples": 3.69, "berries": 4.00, "chocolate": 2.89, "turkey": 6.99, "cheese": 4.00, "pepsi": 7.89, "eggs": 3.50, "bread": 3.00}
    #call the show_available_items function
    show_available_items(items)

    #call the add_item function
    cart = add_items(items)
    print(cart)

    #display items in cart
    print()
    print("the items currently in your cart are: ")
    for items in cart:
        print(items)

    #call the get_total function
    cart_total = get_total(cart, items)
    print(f"{cart_total:.2f}")
    
    disperse_change(83)

#call the main
main()
