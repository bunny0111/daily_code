'''
Write a python program to calculate the factorial of a number.
'''
# number = int(input("Enter the number you want to check="))
# fact = 1
# for i in range(1, number+1):
#     fact = fact * i
# print(fact)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input("Enter number="))
print(f"The factorial of {num} is {factorial(num)}.")