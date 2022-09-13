#!/usr/bin/env python3

# Here is another example of the use of while:

a = 1
s = 0
print('Enter Numbers to add to the sum.')
print('Enter 0 to quit.')
while a != 0:                           
    print('Current Sum:', s)            
    a = float(input('Number? '))        
    s = s + a                            
print('Total Sum =', s)

# Notice how print('Total Sum =', s) is only run at the end. The while statement only affects the lines that are indented with whitespace. The != means does not equal so while a != 0: means as long as a is not zero run the tabbed statements that follow.

# Note that a is a floating point number, and not all floating point numbers can be accurately represented, so using != on them can sometimes not work. Try typing in 1.1 in interactive mode.