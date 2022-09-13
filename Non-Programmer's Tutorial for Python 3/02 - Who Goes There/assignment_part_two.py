#!/usr/bin/env python3

number = float(input("Type in a number: "))
integer = int(input("Type in an integer: "))
text = input("Type in a string: ")
print("number =", number)
print("number is a", type(number))
print("number * 2 =", number * 2)
print("integer =", integer)
print("integer is a", type(integer))
print("integer * 2 =", integer * 2)
print("text =", text)
print("text is a", type(text))
print("text * 2 =", text * 2)

# Notice that number was created with float(input()) ,int(input()) returns an integer, a number with no decimal point, while text created with input() returns a string(can be writen as str(input()), too). When you want the user to type in a decimal use float(input()), if you want the user to type in an integer use int(input()), but if you want the user to type in a string use input().

# The second half of the program uses the type() function which tells what kind a variable is. Numbers are of type int or float, which are short for integer and floating point (mostly used for decimal numbers), respectively. Text strings are of type str, short for string. Integers and floats can be worked on by mathematical functions, strings cannot. Notice how when python multiplies a number by an integer the expected thing happens. However when a string is multiplied by an integer the result is that multiple copies of the string are produced (i.e., text * 2 = HelloHello).

# Operations with strings do different things than operations with numbers. As well, some operations only work with numbers (both integers and floating point numbers) and will give an error if a string is used. Here are some interactive mode examples to show that some more.