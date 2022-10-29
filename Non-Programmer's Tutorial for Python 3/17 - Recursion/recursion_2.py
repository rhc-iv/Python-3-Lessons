#!/usr/bin/env python3

def main():
    num = int(input("Please enter a non-negative integer.\n"))
    fact = factorial(num)
    print("The factorial of",num,"is",fact)

def factorial(num):
    if num == 0:
        return  1
    else:
        return num * factorial(num - 1)

main()