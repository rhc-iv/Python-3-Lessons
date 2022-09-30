#!/usr/bin/env python 3

#This program asks a user for a name and a password.
# It then checks them to make sure that the user is allowed in.

name = input("What is your name? ")
password = input("What is the password? ")
if name == "Josh" and password == "Friday":
    print("Welcome Josh")
elif name == "Fred" and password == "Rock":
    print("Welcome Fred")
else:
    print("I don't know you.")

# The program will only parse as 'true' when the correct
# credentials have been entered.  In this case, 'Josh' +
# 'Friday' or 'Fred' + 'Rock' are considered 'true' 
# according to the 'if/else' procedure.