'''deque = Double Ended Queue
It is implemented by Doubly Linked List.
Deque, which stands for Double Ended Queue, is a special type of queue that allows adding and removing elements from both front and rear ends.
'''

# Implementation of stack using Deque

from collections import deque
mystack = deque()
mystack.append('a')
mystack.append('b')
mystack.append('c')
print(mystack)
print(mystack.pop())    # c will be popped
print(mystack.pop())    # b will be popped
print(mystack.pop())    # a will be popped