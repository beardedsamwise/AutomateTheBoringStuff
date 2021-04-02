import re
#Question 20
#WIP
numRegex = re.compile(r'(\d){1,3}(,)?(\d\d\d)?(,)?(\d\d\d)?')
mo = numRegex.search('444,444')
print(mo.group(0))
mo = numRegex.search('444,444,444')
print(mo.group(0))
mo = numRegex.search('4444')
print(mo.group(0))


