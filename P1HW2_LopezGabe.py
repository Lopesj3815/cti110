#This program calculates and displays travel expens
#6/16/23
#CTI-110 P1HW2 - Travel Expense
#Gabe Lopez
#

print('This program calculates and displays travel expenses')
print()
budget=float(input('Enter Budget: '))
print()
travel=input('Enter your travel destination: ')
print()
gas=float(input('How much do you think you will spend on gas? '))
print()
hotel=float(input('Approximately, how much will you need for accomodations? '))
print()
food=float(input('last, how much do you need for food? '))
print()
print()
print("-"*12,"Travel Expenses", "-"*12)
print("Location: " +  travel)
print("Initial Budget:",budget)
print()
print("Fuel Budget:",gas)
print("Accomodation:",hotel)
print("Food:",food)
print()
print("Remaing Balance:",budget - (gas + hotel + food))
