#!/usr/bin/env python3

# One thing to note at this point is that the boolean expression 
# returns a value indicating True or False, but that Python 
# considers a number of different things to have a truth value 
# assigned to them. To check the truth value of any given 
# object x, you can use the function bool(x) to see its truth 
# value.

# 'Zero' or '0' is always parsed as 'false'
a = 0
bool(a)
print("bool(0) is... ")
print(bool(a))
print("")

# 'One' or '1' is always parsed as 'true'
b = 1
bool(b)
print("bool(1) is... ")
print(bool(b))