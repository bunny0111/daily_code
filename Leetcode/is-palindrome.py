def is_palindrome(s):
    s = s.replace(" ", "").lower()
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

s = "A man a plan a canal Panama"
s1 = "Hello"
print(is_palindrome(s))
print(is_palindrome(s1))