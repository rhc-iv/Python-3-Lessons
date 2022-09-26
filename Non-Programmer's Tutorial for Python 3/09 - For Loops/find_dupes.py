#!/usr/bin/env python3

# A program to find out if there are any duplicates in a list like this:

list = [1, 2, 3, 4, 5, 6, 7, 4, 8, 9, 10]
list.sort()
prev = None
for item in list:
    if prev == item:
        print("Duplicate of", prev, "found")
    prev = item