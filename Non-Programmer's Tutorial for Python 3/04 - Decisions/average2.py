#!/usr/bin/env python3

# Asks for number inputs until total count is reached
# Prints the average value of the counted input numbers

# Note: An integer is used to keep track of input count
# Note: Floating point numbers are used for each input

sum = 0.0

print("This program will take several numbers then average them")
count = int(input("How many numbers would you like to average: "))
current_count = 0

while current_count < count:
    current_count = current_count + 1
    print("Number", current_count)
    number = float(input("Enter a number: "))
    sum = sum + number
    
print("The average was:", sum / count)