#!/usr/bin/env python3

from time import time, ctime

prev_time = ""
while True:
    the_time = ctime(time())
    if prev_time != the_time:
        print("The time is:", ctime(time()))
        prev_time = the_time

# 'Ctrl' + 'c' will end this program