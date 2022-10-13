# Here is a simple example of file I/O (input/output):

# Write a file

with open("test.txt", "wt") as out_file:
    out_file.write("This Text is going to an 'out' file\nLook at it and see!")

# Read a file

with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)

# Notice that it wrote a file called test.txt in the 
# directory that you ran the program from. The \n in the 
# string tells Python to put a newline where it is.

# An overview of file I/O is:
#   Get a file object with the open function
#   Read or write to the file object (depending on how it was opened)
#   If you did not use with to open the file, you'd have to close it manually

#The first step is to get a file object. The way to do 
# this is to use the open function. The format is 
# file_object = open(filename, mode) where file_object 
# is the variable to put the file object, filename is a 
# string with the filename, and mode is "rt" to read a 
# file as text or "wt" to write a file as text (and a 
# few others we will skip here). Next the file objects 
# functions can be called. The two most common functions 
# are read and write. The write function adds a string to 
# the end of the file. The read function reads the next thing 
# in the file and returns it as a string. If no argument is 
# given it will return the whole file (as done in the example).