'''
Given a string, write a program to return the sum of the digits that appear in the string, ignoring all other characters.
input = 'pynative29@#8496'   output = 38
'''
a = 'pynative29@#8496'
n = '1234567890'
total = 0
for i in a:
    if i in n:
        total += int(i)
print(total)
