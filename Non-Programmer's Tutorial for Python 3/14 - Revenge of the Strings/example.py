#!/usr/bin/env python3

def shout(string):
    for character in string:
        print("Gimme an " + character)
        print("'" + character + "'")

shout("Lose")

def middle(string):
    print("The middle character is:", string[len(string) // 2])

middle("abcdefg")
middle("The Python Programming Language")
middle("Atlanta")

# What these programs demonstrate is that strings are 
# similar to lists in several ways. The shout() function 
# shows that for loops can be used with strings just as 
# they can be used with lists. The middle procedure shows 
# that that strings can also use the len() function and 
# array indexes and slices. Most list features work on strings 
# as well.