#!/usr/bin/env python3

# Ccalculates a given rectangle area or a square area
# or the area of a circle:

def circle(radius):
  return 3.14 * radius**2

def square(L):
  return L * L

def rectangle(width, height):
  return width * height

def options():
    print()
    print("Options:")
    print("c = calculate the area of a circle.")
    print("r = calculate the area of a rectangle.")
    print("s = calculate the area of a square.")
    print("q = quit")
    print()

print("This program will calculate the area of a circles, rectangle or a square.")
choice = "x"
options()
while choice != "q":
    choice = input("Please enter your choice: ")
    if choice == "c":
        radius = float(input("Radius of the circle: "))
        print("The area of the circle is", circle(radius))
        options()
    elif choice == "r":
        width = float(input("Width of the rectangle: "))
        height = float(input("Height of the rectangle: "))
        print("The area of the rectangle is", rectangle(width, height))
        options()
    elif choice == "s":
        L = float(input("Length of square side: "))
        print("The area of the square is", square(L))
        options()
    elif choice == "q":
        print(" ",end="")
    else:
        print("Unrecognized option.")
        options()