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
number_sandwich = pyip.inputNum(
    min=1, prompt="How many sandwiches would you like?\n")

# define prices for sandwich ingredients 
bread_cost = {'white': 1, 'wheat': 1, 'sourdough': 2}
protein_cost = {'chicken': 3, 'tofu': 2, 'ham': 3, 'turkey': 3}
cheese_cost = 2
toppings_cost = 1

# calculate the cost of the ordered sandwich or sandwiches 
cost = 0
cost += (bread_cost.get(bread))
cost += (protein_cost.get(protein))
if cheese == "yes":
    cost += cheese_cost
if toppings == "yes":
    cost += toppings_cost
cost = cost * number_sandwich

if number_sandwich == 1:
    print("Your sandwich comes to a total of $" + str(cost))
else:
    print("You ordered " + str(number_sandwich) + " sandwiches with a total cost of $" + str(cost))