#!/usr/bin/env python 3

# Asks for name(string) input
# Input your name = That is a nice name.
# Input other name = ... some funny text.
# Otherwise (no input matching 2 elif's or 1 else):
#   = You have a nice name.

name = input('Your name: ')
if name == 'Robert':
    print('That is a nice name.')
elif name == 'John Cleese':
    print('... some funny text.')
elif name == 'Michael Palin':
    print('... some funny text.')
else:
    print('You have a nice name.')