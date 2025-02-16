'''
Write a python program to convert Celcius to Farenheit
Formula:
F = (C × 9/5) + 32 -> c to f
C = (32°F − 32) × 5/9 -> f to c
'''
c = float(input("Enter celcius="))
f = ((c * 9/5) + 32)
print(f"{c} celcius to Farenheit is {f}")

# Farenheit to celcius
f = float(input("Enter farenheit="))
c = ((f - 32) * 5/9)
print(c)