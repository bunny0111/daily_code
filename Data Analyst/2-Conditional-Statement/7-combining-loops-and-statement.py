'''
Write a program that asks the user to input a number and prints all the even numbers from 1 to that number using a for loop.
'''
number = int(input("Enter number="))
for i in range(1, number+1):
    if i%2==0:
        print(i)