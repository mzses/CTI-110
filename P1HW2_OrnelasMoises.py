#Moises Ornelas
#02/21/2024
#P1HW2
#Travel calculator

'''
Ask user to enter budget

Ask user to enter destination

Ask user for amount they will spend on gas

Ask user for amount they will spend on accommodation

Ask user for amount they will spend on food

Add expenses

Subtract expenses from budget

Display results
'''

#ask user for budget

budget = int(input("Enter your budget here: "))

#ask user for destination

destination = input("Enter your travel destination here: ")

#ask user for fuel cost

gas = int(input("How much do you think you'll spend on gas: "))

#ask user for accomodation cost

accomodation = int(input("Enter the amount you need for accomodation purposes: "))

#ask user for amount on food

food = int(input("lastly, how do you think for food: "))



#printing output for user to see



print("---------Travel Expenses---------")
print("Location: ", destination)
print("Your Budget: ", budget)
print("Fuel cost: ", gas)
print("Accomodation cost: ", accomodation)
print("Food cost: ", food)

#make variable that adds all expenses

total_spent = int(gas + accomodation + food)

#make variable that subtracts all expenses from the budget

remaining_balance = int(budget - total_spent)



#print remaining balance




print("Remaining Balance: ", remaining_balance)




