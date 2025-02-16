'''
Write a python program to swap the values of two variables.
'''
num1 = int(input("Enter the first number="))
num2 = int(input("Enter the second number="))
print(f"Number before swap: first {num1} and second {num2}")
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(f"Number after swap: first {num1} and second {num2}")


'''
num1 = int(input("Enter the first number="))
num2 = int(input("Enter the second number="))
print(f"Number before swap: first {num1} and second {num2}")
num1, num2 = num2, num1
print(f"Number after swap: first {num1} and second {num2}")
'''