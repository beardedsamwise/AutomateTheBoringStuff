import random
streakExists = 0
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
        streakExists += 1
    elif (results.find('TTTTTT')):
        streakExists += 1
# Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (streakExists / 100))

