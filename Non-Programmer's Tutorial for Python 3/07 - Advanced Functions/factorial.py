#!/usr/bin/env python3

# Defines a function that calculates the factorial

def factorial(n):
    if n == 0:
        return 1
    if n<0:
        return "Error, negative numbers do not have factorial values!!"
    return n * factorial(n - 1)

print("2! =", factorial(2))
print("3! =", factorial(3))
print("4! =", factorial(4))
print("5! =", factorial(5))
print("-3! =", factorial(-3))