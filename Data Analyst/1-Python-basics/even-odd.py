'''
Write a python program to check if a number is even or odd.
'''
num = int(input("Enter the number="))
if num == 0:
    print("You have entered Zero.")
elif num%2 == 0:
    print(f"{num} is even number.")
else:
    print(f"{num} is odd number.")