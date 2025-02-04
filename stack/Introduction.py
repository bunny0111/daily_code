'''Stack is a last in, first out (LIFO) structure'''

# Implementation of stack using List Data Structure

stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
print(stack.pop())  # c removed
print(stack.pop())  # b removed
print(stack.pop())  # a removed