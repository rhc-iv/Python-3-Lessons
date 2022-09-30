#!/usr/bin/env python3

# Write a program that has a user guess your name, but they 
# only get 3 chances to do so until the program quits.

print("Try to guess my name!")
count = 1
name = "robert"
guess = input("What is my name? ")

# '.lower' allows things like 'Robert' to still match!

while count < 3 and guess.lower() != name:
    print("You are wrong!")
    guess = input("What is my name? ")
    count = count + 1

if guess.lower() != name:
    print("You are wrong!") 

# This message isn't printed on the third chance, so we print it now!

    print("You ran out of chances.")
else:
    print("Yes! My name is", name + "!")