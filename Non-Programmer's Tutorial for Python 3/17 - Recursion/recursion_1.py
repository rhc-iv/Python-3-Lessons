#!/usr/bin/env python3

# Program by Mitchell Aikens
# No copyright
# 2012
def main():
    loopnum = int(input("How many times would you like to loop?\n"))
    counter = 1
    recurr(loopnum,counter)

def recurr(loopnum,counter):
    if loopnum > 0:
        print("This is loop iteration",counter)
        recurr(loopnum - 1,counter + 1)
    else:
        print("The loop is complete.")

main()