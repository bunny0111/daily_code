'''
Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.
'''
total = 0
while True:
    number = int(input("Enter any number (0 to stop)= "))
    if number == 0:
        break
    total += number
print(f"The sum of all the numbers is {total}")