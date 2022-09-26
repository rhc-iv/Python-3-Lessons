#!/usr/bin/env python3

# Notice how the for loop goes through and sets item to each 
# element in the list. So, what is for good for? The first use 
# is to go through all the elements of a list and do something 
# with each of them. Here's a quick way to add up all the elements:

list = [10, 20, 6, 6]
sum = 0
for num in list:
    sum = sum + num
print("Adding 10 plus 20 plus 6 plus 6...")
print("The sum is: ", sum)