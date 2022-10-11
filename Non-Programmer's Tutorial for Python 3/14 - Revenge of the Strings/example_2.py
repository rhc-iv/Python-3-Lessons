#!/usr/bin/env python3

def to_upper(string):
    ## Converts a string to upper case
    upper_case = ""
    for character in string:
        if 'a' <= character <= 'z':
            location = ord(character) - ord('a')
            new_ascii = location + ord('A')
            character = chr(new_ascii)
        upper_case = upper_case + character
    return upper_case

print(to_upper("This is Text"))

# This works because the computer represents the 
# characters of a string as numbers from 0 to 1,114,111. 
# \For example 'A' is 65, 'B' is 66 and א is 1488. 
# The values are the unicode value. Python has a function 
# called ord() (short for ordinal) that returns a character 
# as a number. There is also a corresponding function called 
# chr() that converts a number into a character. With this 
# in mind the program should start to be clear. The first 
# detail is the line: if 'a' <= character <= 'z': which 
# checks to see if a letter is lower case. If it is then 
# the next lines are used. First it is converted into a 
# location so that a = 0, b = 1, c = 2 and so on with the 
# line: location = ord(character) - ord('a'). Next the new 
# value is found with new_ascii = location + ord('A'). 
# This value is converted back to a character that is now 
# upper case. Note that if you really need the upper case 
# of a letter, you should use u=var.upper() which will work 
# with other languages as well.