# Write a function that uses regular expressions to make sure the password string it is passed is strong. 
# A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.
import re

def passStrength(password):
    capsRegex = re.compile(r'([A-Z])') # regex for capital letters
    lowRegex = re.compile(r'([a-z])') # regex for lower case letters
    numRegex = re.compile(r'\d') # regex for numbers
    numMo = numRegex.findall(password) # find all numbers
    alphaMo = capsRegex.findall(password) + lowRegex.findall(password) # combine regex results for all letters
    lowMo = lowRegex.findall(password) # find all lower case chars
    capsMo = capsRegex.findall(password) # find all upper case chars 

    print("Current password is: " + password) # You'd never do this with a real password

    # check there are 8 letters, 1 number, and a mix of upper and lower case
    if (len(numMo) > 0 and len(alphaMo) > 7 and len(lowMo) > 0 and len(capsMo) > 0):
        print("Your password is valid!")
    else:
        print("Your password does not meet the minimum requirements.")
        print("It must contain 8 letters with a mix of lower and upper case and 1 number.")
    print("")

passStrength("AbCdEfGhIjKl21")
passStrength("AbCdEfG1")
passStrength("AbCdEfGasd")
passStrength("abcdefghji12")
