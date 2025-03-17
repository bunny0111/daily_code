'''
Check if a string is a palindrome 
Question: Write a function to check if a string is a palindrome
Input: "madam"
Output: True
'''

def is_palindrome(s):
    # Setting 2-pointers
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        
        i += 1
        j -= 1
    return True
        
print(is_palindrome('madam'))
print(is_palindrome('shubham'))

'''
The **while loop condition** in `while i < j:` ensures that the loop runs as long as the left pointer (`i`) is **before** the right pointer (`j`).  

### **Explanation:**
- `i` starts at the beginning (`0`), and `j` starts at the end (`len(s) - 1`).
- The loop checks if `s[i]` (left character) and `s[j]` (right character) are the same.
- If they don’t match, the function returns `False` immediately.
- If they match, both pointers move inward (`i += 1`, `j -= 1`).
- The loop stops when `i` is **no longer less than** `j`, meaning:
  - Either all characters have been checked, confirming the string is a palindrome.
  - Or a mismatch was found earlier, returning `False`.

### **Key Insight:**

- The loop ensures only half of the string is checked, optimizing performance.
- When `i == j` (odd-length string) or `i > j` (even-length string), all necessary checks are complete.
'''