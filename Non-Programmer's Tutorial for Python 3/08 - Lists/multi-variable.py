#!/usr/bin/evn python3

# You have already seen ordinary variables that store a 
# single value. However other variable types can hold more 
# than one value. These are called containers because they 
# can contain more than one object. The simplest type is 
# called a list. Here is an example of a list being used:

which_one = int(input("What month (1-12)? "))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

if 1 <= which_one <= 12:
    print("The month is", months[which_one - 1])

# In this example the months is a list. months is defined with the lines months
# = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
# and 'August', 'September', 'October', 'November', 'December'] 
# (note that a \ could also be used to split a long line, but that 
# is not necessary in this case because Python is intelligent enough 
# to recognize that everything within brackets belongs together). 
# The [ and ] start and end the list with commas (,) separating the 
# list items. The list is used in months[which_one - 1]. A list consists 
# of items that are numbered starting at 0. In other words if you 
# wanted January you would use months[0]. Give a list a number and 
# it will return the value that is stored at that location.

# The statement if 1 <= which_one <= 12: will only be true if 
# which_one is between one and twelve inclusive (in other words 
# it is what you would expect if you have seen that in algebra).