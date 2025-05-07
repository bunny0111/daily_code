'''
Given a string, print the final string by pushing all the odd index characters to the end and all the even index charaters to the beginning of the string.
input = "abcabc" output = "acbbac"
'''
a = "abcabc"
x = ""
y = ""

for i in range(len(a)):
    if i % 2 == 0:
        x += a[i]
    else:
        y += a[i]

print(x+y)