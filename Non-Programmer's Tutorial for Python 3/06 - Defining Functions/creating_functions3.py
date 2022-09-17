#!/usr/bin/env python3

# Notice how the values of a and b are not changed in the previous example. 
# Functions can be used to repeat tasks that don't return values. Here is an example:

def hello():
    print("Hello")

def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

hello()
hello()

print_welcome("Fred")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

# This example shows some more stuff that you can do with functions. 
# Notice that you can use no arguments or two or more. 
# Notice also when a function doesn't need to send back a value, a return is optional.