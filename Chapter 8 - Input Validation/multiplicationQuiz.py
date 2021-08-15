import pyinputplus as pyip
import random
import time

correct_answers = 0

print("This program will ask you 10 multiplication questions.")
print("You'll have three atetempts at each question and 8 seconds to respond")
print("Good luck!\n")

for i in range(0, 10):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    result = x * y
    print("Question " + str(i + 1) + ":")
    print("What is " + str(x) + " x " + str(y) + "?")
    for i in range(0, 3):
        try:
            answer = pyip.inputNum(timeout=8)
        except pyip.TimeoutException:
            print("You took longer than 8 seconds to respond!")
            answer = 0
        if answer == result:
            correct_answers += 1
            print("That's correct!")
            time.sleep(1)
            break
        elif i < 2:
            print("Try again!")
        else:
            print("Sorry, you only get three attempts.")
        time.sleep(1)

print("\nYou answered " + str(correct_answers) +
      " question correctly. Well done!")
