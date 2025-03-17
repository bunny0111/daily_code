'''
Find the index of the First Non-repeating character

Question: Write the function to find the index of non-repeating character in a string.
Input: 'SWISS'
Output: 1 (The character 'S' repeats, but 'w' is the first non-repeating).
'''

def non_repeating(s):
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i
    return -1

print(non_repeating('swiss'))
print(non_repeating('aaaaa'))