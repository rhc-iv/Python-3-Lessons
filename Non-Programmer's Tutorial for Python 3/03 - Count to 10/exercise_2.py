#!/usr/bin/env python3

# If you would like the program to run continuously, just add a while 1 == 1: loop around the whole thing. You will have to indent the rest of the program when you add this at the top of the code, but don't worry, you don't have to do it manually for each line! Just highlight everything you want to indent and click on "Indent" under "Format" in the top bar of the python window.

# Another way of doing this could be:

name = input('Set name: ')
password = input('Set password: ')
while 1 == 1:
    nameguess=""
    passwordguess=""
    key=""
    while (nameguess != name) or (passwordguess != password):
        nameguess = input('Name? ')
        passwordguess = input('Password? ')
    print("Welcome,", name, ". Type lock to lock.")
    while key != "lock":
        key = input("")

# Notice the or in while (nameguess != name) or (passwordguess != password), which we haven't yet introduced. You can probably figure out how it works.