import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    results = ''
    for experimentNumber in range(100):
        coinFlip = random.randint(0, 1)
        if coinFlip == 0:
            results += 'H'
        else:
            results += 'T'
    if (results.find('HHHHHH')):
        numberOfStreaks += 1
    elif (results.find('TTTTTT')):
        numberOfStreaks += 1
    #print(results)
# Code that checks if there is a streak of 6 heads or tails in a row.
# Not actually sure if this is mathemetically accurate, but seems close 
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

