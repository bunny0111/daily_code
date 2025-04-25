'''
Input:- s = "anagram" t = "nagaram" Output:- True
Input:- s = "rat" t = "car" Output:- False
'''
from collections import Counter
def valid_anagram(s,t):
    return Counter(s) == Counter(t)

s = "anagram" 
t = "nagaram"
s1 = "rat"
s2 = "car"
print(valid_anagram(s, t))
print(valid_anagram(s1, s2))


def is_anagram(a,b):
    return sorted(a) == sorted(b)
print(is_anagram(s, t))
print(is_anagram(s1, s2))