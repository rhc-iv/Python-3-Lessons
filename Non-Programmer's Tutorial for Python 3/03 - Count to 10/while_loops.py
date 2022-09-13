#!/usr/bin/env python3

# Presenting our first control structure. Ordinarily the computer starts with the first line and then goes down from there. Control structures change the order that statements are executed or decide if a certain statement will be run. Here's the source for a program that uses the while control structure:

# FIRST, set the initial value of the variable a to 0(zero).
a = 0

# While the value of the variable a is less than 10 do the following:
while a < 10:

# Increase the value of the variable a by 1, as in: a = a + 1!
    a = a + 1

# Print to screen what the present value of the variable a is.
    print(a)     

# REPEAT! until the value of the variable a is equal to 9!? See note. 

# NOTE:
# The value of the variable a will increase by 1
# with each repeat, or loop of the 'while statement BLOCK'.
# e.g. a = 1 then a = 2 then a = 3 etc. until a = 9 then...
# the code will finish adding 1 to a (now a = 10), printing the 
# result, and then exiting the 'while statement BLOCK'. 
#              --
# While a < 10: |
#     a = a + 1 |<--[ The while statement BLOCK ]
#     print (a) |
#
# So what does the program do? First it sees the line a = 0 and sets a to zero. Then it sees while a < 10: and so the computer checks to see if a < 10. The first time the computer sees this statement, a is zero, so it is less than 10. In other words, as long as a is less than ten, the computer will run the tabbed in statements. This eventually makes a equal to ten (by adding one to a again and again) and the while a < 10 is not true any longer. Reaching that point, the program will stop running the indented lines.

# Always remember to put a colon ":" at the end of the while statement line!