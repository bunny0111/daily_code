'''
Write a program that prints the first n fibonacci numbers, where n is input by the user.
'''
n = int(input("Enter a number="))
a, b = 0, 1
count = 0
while count<n:
    print(a)
    a, b = b, a + b
    count += 1