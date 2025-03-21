'''
Write a program to check if a string is palindrome or not
'''

def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        
        i += 1
        j -= 1
    return True

print(is_palindrome("madam"))
print(is_palindrome("shubham"))