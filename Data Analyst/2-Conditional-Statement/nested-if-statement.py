'''
Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd, or negative
'''
n = int(input("Enter number="))
if n==0:
    print("Number is zero.")
elif n>0:
    if n % 2 == 0:
        print(f"{n} is positve even number.")
    else:
        print(f"{n} is positve odd number.")
else:
    print(f"{n} is negative number.")