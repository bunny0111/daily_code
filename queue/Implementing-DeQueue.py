# In dequeu we and append and pop from the both side

import collections
q = collections.deque()

q.appendleft(10)    # By default append works on right side of the list.
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)
print(q)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
# This perform the FIFO methods

# One more method to perform FIFO methods
q1 = collections.deque()
q1.append(60)
q1.append(70)
q1.append(80)
q1.append(90)
print(q1)
print(q1.popleft()) # 60 removed
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())
