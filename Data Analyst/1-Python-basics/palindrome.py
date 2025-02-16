'''
Write a python program to check if a string is palindrome or not
'''
string = input("Enter string=")
if string == string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")