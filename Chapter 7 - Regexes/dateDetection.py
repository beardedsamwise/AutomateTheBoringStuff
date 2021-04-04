import re

def isValidDate(date):
    # create regex to find dates in dd/mm/yyyy format
    dateRegex = re.compile(r'(\d{2})(/)(\d{2})(/)(\d{4})')
    mo = dateRegex.search(date)

    # set variables 
    validDate = False
    leapYear = False
    day = int(mo.group(1))
    month = int(mo.group(3))
    year = int(mo.group(5))
    regMonths = [1,3,5,7,8,10,12] # months with 31 days
    shortMonths = [4,6,9,11] # months with 30 days 

    # check for leap year 
    if (year % 4 == 0) and (year % 100 != 0):
        leapYear = True
    if (year % 400 == 0):
        leapYear = True

    # check April, June, September, and November which have 30 days
    if month in shortMonths:
        if day > 0 and day < 31:
            validDate = True

    # check February which has 28 days (non leap years)
    if (month == 2) and (leapYear == False):
        if day > 0 and day < 29:
            validDate = True
        
    # check February which has 29 days in leap years
    if (month == 2) and (leapYear == True):
        if day > 0 and day < 30:
            validDate = True

    # check all other dates
    if month in regMonths:
        if day > 0 and day < 32:
            validDate = True
    
    print(validDate)

isValidDate('The date is 22/10/2020') #true
isValidDate('The date is 30/02/2020') #false
isValidDate('The date is 29/02/2020') #true
isValidDate('The date is 29/02/2021') #false
isValidDate('The date is 28/02/2021') #true


