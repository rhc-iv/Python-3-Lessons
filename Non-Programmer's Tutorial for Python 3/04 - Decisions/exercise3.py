#!/usr/bin/env python3

# Asks for 2 input numbers
# Sums the inputs and:
#   If the input sum >100, returns "That is a big number"
#   If the input sum <100, exits the script

number1 = float(input('1st number: '))
number2 = float(input('2nd number: '))
if number1 + number2 > 100:
    print('That is a big number.')