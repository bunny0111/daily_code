'''
Write a program that calculates the factorial of a number input by the user a while loop
'''
number = int(input("Enter number="))
fact = 1
i = 1
while i <= number:
    fact *= i
    i += 1
print(f"The factorial of {number} is {fact}")