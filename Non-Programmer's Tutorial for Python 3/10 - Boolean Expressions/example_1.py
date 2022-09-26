#!/usr/bin/env python3

# Here is a little example of boolean expressions:

a = 6
b = 7
c = 42
print(1, a == 6)
print(2, a == 7)
print(3, a == 6 and b == 7)
print(4, a == 7 and b == 7)
print(5, not a == 7 and b == 7)
print(6, a == 7 or b == 7)
print(7, a == 7 or b == 6)
print(8, not (a == 7 and b == 6))
print(9, not a == 7 and b == 6)

# What is going on? The program consists of a bunch 
# of funny looking print statements. Each print statement 
# prints a number and an expression. The number is to 
# help keep track of which statement I am dealing with. 
# Notice how each expression ends up being either False 
# or True. In Python false can also be written as 0 and 
# true as 1.

# The behavior of 'and' operator can be summarized as follows:

# Expression:                            Result:
# true and true                          true
# true and false                         false
# false and true                         false
# false and false                        false
# The last 3 examples are false, since Python checks
# both the first 'and' last parts of the expression
# to calculate a Boolean result.

# The behavior of 'not' operator can be summarized as follows:

# Expression                             Result
# not true                               false
# not false                              true
# Using 'not', Python will return a Boolean result that
# is the opposite of the 'not' expression.

# The behavior of the 'or' operator can be summarized as follows:

# Expression                             Result
# true or true                           true
# true or false                          true
# false or true                          true
# false or false                         false
# The first 3 examples are true, since Python checks the first
# expression via 'or', returning true for the first half regardless
# of the second half of the expression