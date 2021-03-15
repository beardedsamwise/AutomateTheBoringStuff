text = {'agree': "Yes, I agree. That sounds fine to me.",
    'busy': "Sorry, can we do this later this week or next week?",
    'upsell': "Would you like fries with that?"}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

print('argv len is ' + str(len(sys.argv)))
print(str(sys.argv[0]))
print(str(sys.argv[1]))

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)