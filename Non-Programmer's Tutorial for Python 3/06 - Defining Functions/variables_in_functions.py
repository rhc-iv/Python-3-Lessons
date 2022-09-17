#!/usr/bin/env python3

# When eliminating repeated code, you often have variables in the repeated code. 
# In Python, these are dealt with in a special way. So far all variables we have seen are global variables. 
# Functions have a special type of variable called local variables. 
# These variables only exist while the function is running. 
# When a local variable has the same name as another variable (such as a global variable), the local variable hides the other. 
# Sound confusing? Well, this next example (which is a bit contrived) should help clear things up.

a = 4

def print_func():
    a = 17
    print("in print_func a =", a)

print_func()
print("a = ", a)

# Variable assignments inside a function do not override global variables, they exist only inside the function. 
# Even though a was assigned a new value inside the function, this newly assigned value was only relevant to print_func, when the function finishes running, and the a's values is printed again, we see the originally assigned values.