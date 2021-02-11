import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

#####################################
###           Variables           ###
# Number of experiments
numExperiments = 10000
# Number of coin flips per experiment
numFlips = 100
# Streak number 
howMany = 6
#####################################



# Create array to search for in results
heads = howMany*'H'
tails = howMany*'T'

# Streak counter
streakExists = 0

# Number of streaks per experiment
numStreaksHeads = []
numStreaksTails = []


for experimentNumber in range(numExperiments):
    # Code that creates a list of 100 'heads' or 'tails' values.
    results = ''
    for experimentNumber in range(numFlips):
        coinFlip = random.randint(0, 1)
        # Convert result to char for code clarity 
        if coinFlip == 0:
            results += 'H' 
        else:
            results += 'T'
    
    # Find streaks
    if (results.find(heads)):
        streakExists += 1
    elif (results.find(tails)):
        streakExists += 1

    numStreaksHeads.append(results.count(heads))
    numStreaksTails.append(results.count(tails))
        

# Print result
print('Chance of streak: %s%%' % ((float(streakExists) / numExperiments)*100))

# Plot result
# TODO: merge heads and tails results and plot 
# Find limits and define bins 
xAxisLim = max(numStreaksHeads)

countHeads = Counter(numStreaksHeads)
countTails = Counter(numStreaksTails)
yAxisLim = max(countHeads.most_common()[0][1], countTails.most_common()[0][1])
bins = np.linspace(-0.5, xAxisLim+0.5, xAxisLim+2)

plt.hist(numStreaksHeads, bins = bins, facecolor='g', alpha=0.5, label='heads')
plt.hist(numStreaksTails, bins= bins,  facecolor='b', alpha=0.5, label='tails')

plt.xlim(0, xAxisLim*1.1)
plt.ylim(0, yAxisLim*1.3)

plt.ylabel('Total Streaks')
plt.xlabel('Number of streaks per experiment')

# Create title
title = "Trials: {0}, Flips per trial: {1}, Streak definition: {2} in a row".format(numExperiments, numFlips, howMany)
plt.title(title)

plt.legend()
plt.show()