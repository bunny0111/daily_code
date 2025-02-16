'''
Write a python program to check if a number is positive, negative or zero.
'''
number = float(input("Enter any number= "))
if number > 0:
    print(f"{number} is positive number.")
elif number < 0:
    print(f"{number} is negative number.")
else:
    print("You have entered Zero (0).")