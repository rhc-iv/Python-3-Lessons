#!/usr/bin/env python3

# Program by Mitchell Aikens
# No Copyright
# 2010

num = 0

def main():
    counter(num)

def counter(num):
    print(num)
    num += 1
    counter(num)

main()