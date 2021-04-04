import re

#Question 21
# Write a regex that matches the full name of someone whose last name is Watanabe. 
# You can assume that the first name that comes before it will always be one word that begins with a capital letter.

watanabeRegex = re.compile(r'([A-Z])(\w)+(\s)Watanabe$')

print(watanabeRegex.search('haruto Watanabe')) #must not match
print(watanabeRegex.search('Mr. Watanabe'))    #must not match
print(watanabeRegex.search('Watanabe'))        #must not match
print(watanabeRegex.search('Haruto watanabe')) #must not match
print(watanabeRegex.search('Haruto Watanabe')) #must match