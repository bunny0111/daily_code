'''Implement stack using Queue module'''

# Queue = FIFo

from queue import LifoQueue
stack = LifoQueue(maxsize=4)
stack.put('a')  # put worked as append in LifoQueue
stack.put('b')
stack.put('c')
print("Full=", stack.full())    # Full is showing False because we have initialized max size is 4 and we have entered 3 values
print("Size=", stack.qsize())
print(stack.get()) # get worked as pop in LifoQueue
print(stack.get())
print(stack.get())
print("Empty=", stack.empty())