#!/usr/bin/env python3 

# Program by Mitchell Aikens
# No Copyright
# 2012

# Procedure 1
def main():
    try:
        # Get a number to maniuplate
        num = float(input("Please enter a number to manipulate.\n"))
        
        # Store the result of the value, after it has been manipulated
        # by Procedure 2
        addednum = addfive(num)
        
        # Store the result of the value, after it has been manipulated
        # by Procedure 3
        multipliednum = multiply(addednum)
        
        # Send the value to Procedure 4
        display(multipliednum)
    
    # Deal with exceptions from non-numeric user entry
    except ValueError:
        print("You must enter a valid number.\n")
        
        # Reset the value of num, to clear non-numeric data.
        num = 0
        
        # Call main, again.
        main()

# Procedure 2
def addfive(num):
    return num + 5

# Procedure 3
def multiply(addednum):
    return addednum * 2.452

# Procedure 4
def display(multi):
    # Display the final value
    print("The final value is ",multi)

# Call Procedure 1
main()