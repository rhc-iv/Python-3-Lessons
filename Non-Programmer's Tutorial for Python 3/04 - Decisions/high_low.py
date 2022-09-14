#!/usr/bin/env python3

# This creates a guessing game of "Higher or Lower"

# This is something that should be semi-random like the last digits of the time or something else; but that will have to wait 'til a later chapter.

number = 7
guess = -1
print("Guess the number!")
while guess != number:
    guess = int(input("Is it..."))
    if guess == number:
        print("Horray! You guessed the number correctly!")
    elif guess < number:
        print("Sorry, the number is larger...")
    elif guess > number:
        print("Sorry, the number is smaller...")