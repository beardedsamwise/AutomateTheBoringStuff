import pyinputplus as pyip

# collect sandwich inputs
bread = pyip.inputMenu(['white', 'wheat', 'sourdough'],
                       prompt="Select your bread type:\n", numbered=True)
protein = pyip.inputMenu(['chicken', 'tofu', 'ham', 'turkey'],
                         prompt="Select your protein:\n", numbered=True)
cheese = pyip.inputYesNo(prompt="Would you like cheese?\n")
if cheese == "yes":
    cheeseType = pyip.inputMenu(
        ['cheddar', 'Swiss', 'mozzarella'], prompt="Select your cheese type:\n", numbered=True)
toppings = pyip.inputYesNo(
    prompt="Would you like lettuce, tomato, mayo and mustard?\n")
numSandwhichs = pyip.inputNum(
    min=1, prompt="How many sandwiches would you like?\n")

# TO DO define prices
bread_cost = {'white': 1, 'wheat': 1, 'sourdough': 2}
protein_cost = {'chicken': 3, 'tofu': 2, 'ham': 3, 'turkey': 3}
cheese_cost = 2
toppings = 1

# TO DO calculate sandwhich cost and return to user
