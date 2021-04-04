import re

# Question 21
# Write a regex that matches the full name of someone whose last name is Watanabe. 
# You can assume that the first name that comes before it will always be one word that begins with a capital letter.

watanabeRegex = re.compile(r'([A-Z])(\w)+(\s)Watanabe$')

print(watanabeRegex.search('haruto Watanabe')) #must not match
print(watanabeRegex.search('Mr. Watanabe'))    #must not match
print(watanabeRegex.search('Watanabe'))        #must not match
print(watanabeRegex.search('Haruto watanabe')) #must not match
print(watanabeRegex.search('Haruto Watanabe')) #must match

# Question 22
# Write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; 
# the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; 
# and the sentence ends with a period? This regex should be case-insensitive.

regex22 = re.compile(r'(alice|bob|carol)\s(eats|pets|throws)\s(apples|cats|baseballs)(.)', re.IGNORECASE)

print(regex22.search('Alice eats apples.'))
print(regex22.search('Bob pets cats.'))
print(regex22.search('Carol throws baseballs.'))
print(regex22.search('Alice throws Apples.'))
print(regex22.search('BOB EATS CATS.'))
print(regex22.search('RoboCop eats apples.'))
