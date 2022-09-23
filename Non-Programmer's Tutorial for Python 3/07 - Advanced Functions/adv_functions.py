#!/usr/bin/evn python3

def mult(a, b):
    if b == 0:
        return 0
    rest = mult(a, b - 1)
    value = a + rest
    return value
result = mult(3, 2)
print("3 * 2 = ", result)

# Basically this program creates a positive integer multiplication 
# function (that is far slower than the built in multiplication function) 
# and then demonstrates this function with a use of the function. 
# This program demonstrates the use of recursion, that is a form 
# of iteration (repetition) in which there is a function that repeatedly 
# calls itself until an exit condition is satisfied. It uses repeated 
# additions to give the same result as multiplication: e.g. 3 + 3 (addition) 
# gives the same result as 3 * 2 (multiplication).