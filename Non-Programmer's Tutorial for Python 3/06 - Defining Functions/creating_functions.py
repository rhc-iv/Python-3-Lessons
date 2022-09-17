#!/usr/bin/env python3

# To start off this chapter I am going to give you an example of what you could do but shouldn't:

a = 23
b = -23

if a < 0:
    a = -a
if b < 0:
    b = -b
if a == b:
    print("The absolute values of", a, "and", b, "are equal.")
else:
    print("The absolute values of", a, "and", b, "are different.")

# The program seems a little repetitive. Programmers hate to repeat things -- that's what computers are for, after all! (Note also that finding the absolute value changed the value of the variable, which is why it is printing out 23, and not -23 in the output.) Fortunately Python allows you to create functions to remove duplication. (See version 2 of this same file!)