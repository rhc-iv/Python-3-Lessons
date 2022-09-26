#!/usr/bin/env python3

# The other way to use for loops is to do something a 
# certain number of times. Here is some code to print 
# out the first 9 numbers of the Fibonacci series:

a = 1
b = 1
for c in range(1, 10):
    print(a, end=" ")
    n = a + b
    a = b
    b = n

# Everything that can be done with for loops can also 
# be done with while loops but for loops give an easy 
# way to go through all the elements in a list or to 
# do something a certain number of times.