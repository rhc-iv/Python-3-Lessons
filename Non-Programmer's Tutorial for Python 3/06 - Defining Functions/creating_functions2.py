#!/usr/bin/env python3

# Here is the rewritten example:

a = 23
b = -23

def absolute_value(n):
    if n < 0:
        n = -n
    return n

if absolute_value(a) == absolute_value(b):
    print("The absolute values of", a, "and", b, "are equal.")
else:
    print("The absolute values of", a, "and", b, "are different.")

# The key feature of this program is the def statement. 
    # def (short for define) starts a function definition. 
        # def is followed by the name of the function absolute_value. 
            # Next comes a '(' followed by the parameter n (n is passed from the program into the function when the function is called). 
                # The statements after the ':' are executed when the function is used. 
                    # The statements continue until either the indented statements end or a return is encountered. 
                        # The return statement returns a value back to the place where the function was called. 
                            # We already have encountered a function in our very first program, the print function. 
                                # Now we can make new functions.