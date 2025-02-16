'''
Write a python program to find the sum of the first n natural numbers.
'''
num = int(input("Enter the number="))
natural_number = (num * (num + 1)) // 2
if num==0:
    print("you have entered zero.")
elif num<0:
    print("you have entered negative number.")
else:
    print(f"Sum of {num} natural numbers is {natural_number}")