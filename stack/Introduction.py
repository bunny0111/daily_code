'''Stack is a last in, first out (LIFO) structure
A stack is a linear data structure that follows the principle of Last In First Out (LIFO). This means the last element inserted inside the stack is removed first.
'''

# Implementation of stack using List Data Structure

stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
print(stack.pop())  # c removed
print(stack.pop())  # b removed
print(stack.pop())  # a removed