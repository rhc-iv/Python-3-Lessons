#!/usr/bin/env python3

a_var = 10
b_var = 15
e_var = 25

def a_func(a_var):
    print("in a_func a_var =", a_var)
    b_var = 100 + a_var
    d_var = 2 * a_var
    print("in a_func b_var =", b_var)
    print("in a_func d_var =", d_var)
    print("in a_func e_var =", e_var)
    return b_var + 10

c_var = a_func(b_var)

print("a_var =", a_var)
print("b_var =", b_var)
print("c_var =", c_var)
print("d_var =", d_var)

# In this example the variables a_var, b_var, and d_var are 
# all local variables when they are inside the function a_func. 
# After the statement return b_var + 10 is run, they all cease 
# to exist. The variable a_var is automatically a local variable 
# since it is a parameter name. The variables b_var and d_var are 
# local variables since they appear on the left of an equals sign 
# in the function in the statements b_var = 100 + a_var and 
# d_var = 2 * a_var .

# Inside of the function a_var has no value assigned to it. When 
# the function is called with c_var = a_func(b_var), 15 is assigned 
# to a_var since at that point in time b_var is 15, making the call 
# to the function a_func(15). This ends up setting a_var to 15 when 
# it is inside of a_func.

# As you can see, once the function finishes running, the local 
# variables a_var and b_var that had hidden the global variables 
# of the same name are gone. Then the statement print("a_var = ", a_var) 
# prints the value 10 rather than the value 15 since the local 
# variable that hid the global variable is gone.

# Another thing to notice is the NameError that happens at the 
# end. This appears since the variable d_var no longer exists 
# since a_func finished. All the local variables are deleted when 
# the function exits. If you want to get something from a function, 
# then you will have to use return something.

# One last thing to notice is that the value of e_var remains 
# unchanged inside a_func since it is not a parameter and it 
# never appears on the left of an equals sign inside of the 
# function a_func. When a global variable is accessed inside a 
# function it is the global variable from the outside.

# Functions allow local variables that exist only inside the 
# function and can hide other variables that are outside the function.