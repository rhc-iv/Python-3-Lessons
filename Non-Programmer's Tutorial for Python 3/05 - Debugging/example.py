#!/usr/bin/env python3

number = 5
while number > 1:
    print(".",end=" ")
    number = number - 1
print()

# What is the first line to be run?
#   The first line of the file: number = 5
# What does it do?
#   Puts the number 5 in the variable number.
# What is the next line?
#   The next line is: while number > 1:
# What does it do?
#   Well, while statements in general look at their expression, and if it is true they do the 
#   next indented block of code, otherwise they skip the next indented block of code.
# So what does it do right now?
#   If number > 1 is true then the next two lines will be run.
# So is number > 1?
#   The last value put into number was 5 and 5 > 1 so yes.
# So what is the next line?
#   Since the while was true the next line is: print(".",end=" ")
# What does that line do?
#   Prints one dot and since the extra argument end=" " exists the next printed text will not #   be on a different screen line.
# What is the next line?
#   number = number - 1 since that is following line and there are no indent changes.
# What does it do?
#   It calculates number - 1, which is the current value of number (or 5) subtracts 1 from it, #   and makes that the new value of number. So basically it changes number's value from 5 to #   4.
# What is the next line?
#   Well, the indent level decreases so we have to look at what type of control structure it #   is. It is a while loop, so we have to go back to the while clause which is while number > #   1:
# What does it do?
#   It looks at the value of number, which is 4, and compares it to 1 and since 4 > 1 the 
#   while loop continues.
# What is the next line?
#   Since the while loop was true, the next line is: print(".",end=" ")
# What does it do?
#   It prints a second dot on the line, ending by a space.
# What is the next line?
#   No indent change so it is: number = number - 1
# And what does it do?
#   It takes the current value of number (4), subtracts 1 from it, which gives it 3 and then #   finally makes 3 the new value of number.
# What is the next line?
#   Since there is an indent change caused by the end of the while loop, the next line is: 
#   while number > 1:
# What does it do?
#   It compares the current value of number (3) to 1. 3 > 1 so the while loop continues.
# What is the next line?
#   Since the while loop condition was true the next line is: print(".",end=" ")
# And it does what?
#   A third dot is printed on the line.
# What is the next line?
#   It is: number = number - 1
# What does it do?
#   It takes the current value of number (3) subtracts from it 1 and makes the 2 the new value #   of number.
# What is the next line?
#   Back up to the start of the while loop: while number > 1:
# What does it do?
#   It compares the current value of number (2) to 1. Since 2 > 1 the while loop continues.
# What is the next line?
#   Since the while loop is continuing: print(".",end=" ")
# What does it do?
#   It discovers the meaning of life, the universe and everything. I'm joking. (I had to make #   sure you were awake.) The line prints a fourth dot on the screen.
# What is the next line?
#   It's: number = number - 1
# What does it do?
#   Takes the current value of number (2) subtracts 1 and makes 1 the new value of number.
# What is the next line?
#   Back up to the while loop: while number > 1:
# What does the line do?
#   It compares the current value of number (1) to 1. Since 1 > 1 is false (one is not greater #   than one), the while loop exits.
# What is the next line?
#   Since the while loop condition was false the next line is the line after the while loop #   exits, or: print()
# What does that line do?
#   Makes the screen go to the next line.
# Why doesn't the program print 5 dots?
#   The loop exits 1 dot too soon.
# How can we fix that?
#   Make the loop exit 1 dot later.
# And how do we do that?
#   There are several ways. One way would be to change the while loop to: while number > 0: #   Another way would be to change the conditional to: number >= 1 There are a couple others.