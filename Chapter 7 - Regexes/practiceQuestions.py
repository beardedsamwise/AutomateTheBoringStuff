import re

#Question 21

watanabeRegex = re.compile(r'([A-Z])(\w)+(\s)Watanabe$')

print(watanabeRegex.search('haruto Watanabe')) #must not match
print(watanabeRegex.search('Mr. Watanabe'))    #must not match
print(watanabeRegex.search('Watanabe'))        #must not match
print(watanabeRegex.search('Haruto watanabe')) #must not match
print(watanabeRegex.search('Haruto Watanabe')) #must match