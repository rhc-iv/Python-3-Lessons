#!/usr/bin/env python3

# This app uses the 'randint' library to generate
# a random number between 0 & 99.  It will print
# 'too high' or 'too low' depending on the number
# that the user selects and will print 'Just right'
# upon the user inputting the random number that 
# is generated by the library.

from random import randint
number = randint(0, 99)
guess = -1
while guess != number: 
    guess = int(input ("Guess a number: "))
    if guess > number:
        print("Too high")
    elif guess < number:
            print("Too low")
print("Just right")