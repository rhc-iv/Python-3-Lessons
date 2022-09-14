#!/usr/bin/env python3

# As always, I believe I should start each chapter with a warm-up typing exercise, so here is a short program to compute the absolute value of an integer:

n = int(input("Number? "))
if n < 0:
    print("The absolute value of", n, "is", -n)
else:
    print("The absolute value of", n, "is", n)

# So what does the computer do when it sees this piece of code? First it prompts the user for a number with the statement "n = int(input("Number? "))". Next it reads the line "if n < 0:". If n is less than zero Python runs the line "print("The absolute value of", n, "is", -n)". Otherwise it runs the line "print("The absolute value of", n, "is", n)".

# More formally Python looks at whether the expression n < 0 is true or false. An if statement is followed by an indented block of statements that are run when the expression is true. Optionally after the if statement is an else statement and another indented block of statements. This second block of statements is run if the expression is false.

# There are a number of different tests that an expression can have:
# Operator                  Function
# <                         less than
# <=                        less than or equal to
# >                         greater than
# >=                        greater than or equal to
# ==                        equal
# !=                        not equal