# This program lets the user type in an integer that then 
# keeps calling collatz() on that number until the function returns the value 1
# For more info: https://en.wikipedia.org/wiki/Collatz_conjecture

def collatz(number):
    if (number % 2 == 0):
        return (number // 2)
    else:
        return (3 * number + 1)

print("Enter any number:")
number = input()

try:
    number = int(number)
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError: 
    print("You entered a non-integer!!!")




    
    



