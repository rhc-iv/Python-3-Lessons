#!/usr/bin/env python3

# This program converts Fahrenheit to Celsius

fahr_temp = float(input("Fahrenheit temperature: "))
celc_temp = (fahr_temp - 32.0) *( 5.0 / 9.0)
print("Celsius temperature:", celc_temp)