'''
Write a Python function `are_anagrams(s1: str, s2: str) -> bool` that returns `True` if the strings `s1` and
`s2` are anagrams (contain the same characters in any order), ignoring spaces and case.
Example:
are_anagrams("listen", "silent") True
are_anagrams("hello", "world") False
'''

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))