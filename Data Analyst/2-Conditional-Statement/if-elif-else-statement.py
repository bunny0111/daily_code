'''
Write a program that asks the user to input a number and prints whether the number is positive, negative or zero.
'''
n = float(input("Enter number="))
if n == 0:
    print("number is zero.")
elif n < 0:
    print(f"{n} is negative number.")
else:
    print(f"{n} is positive number.")