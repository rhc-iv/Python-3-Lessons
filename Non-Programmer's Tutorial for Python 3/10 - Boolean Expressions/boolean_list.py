#!/usr/bin/env python3

# Create a list:
list = ["Life", "The Universe", "Everything", "Jack", "Everything", "Life", "Jill"]

# Make a copy of the list. See the 'More on Lists' 
# chapter to explain what [:] means.
copy = list[:]

# Sort the copied list:
copy.sort()
prev = copy[0]
del copy[0]

count = 0

# Go through the list, searching for a match:
while count < len(copy) and copy[count] != prev:
    prev = copy[count]
    count = count + 1

# If a match was not found, then count can't be < len
# since the while loop continues while count is < len
# and no match is found
if count < len(copy):
    print("First Match:", prev)

# This program works by continuing to check for match 
# while count < len(copy) and copy[count] is not equal 
# to prev. When either count is greater than the last 
# index of copy or a match has been found the and is 
# no longer true so the loop exits. The if simply checks 
# to make sure that the while exited because a match was found.

# The other "trick" of and is used in this example. If 
# you look at the table for and notice that the third 
# entry is "false and false". If count >= len(copy) (in 
# other words count < len(copy) is false) then copy[count] 
# is never looked at. This is because Python knows that 
# if the first is false then they can't both be true. This 
# is known as a short circuit and is useful if the second 
# half of the and will cause an error if something is wrong. 
# I used the first expression (count < len(copy)) to check 
# and see if count was a valid index for copy. (If you don't 
# believe me remove the matches "Jill" and "Life", check that 
# it still works and then reverse the order of count < len(copy) 
# and copy[count] != prev to copy[count] != prev and count < len(copy).)

# Boolean expressions can be used when you need to check 
# two or more different things at once.