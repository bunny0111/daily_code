'''
Write a Python function `count_vowels(s: str) -> int` that returns the number of vowels (a, e, i, o, u) in the
string `s`, ignoring case.
Example:
count_vowels("Hello World") 3
count_vowels("Python") 1
'''
def count_vowel(s):
    vowel = 0
    for i in s:
        if (i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
            vowel += 1
    return vowel
s = 'Hello World'
print(count_vowel(s))