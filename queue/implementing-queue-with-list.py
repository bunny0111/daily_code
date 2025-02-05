queue = []
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
print(queue.pop())  # removed 30
print(queue.pop())  # removed 20
print(queue.pop())  # removed 10

# First in first out(FIFO)
queue1 = []
queue1.insert(0, 10)
queue1.insert(0, 20)
queue1.insert(0, 30)
print(queue1)
print(queue1.pop())
print(queue1.pop())
print(queue1.pop())
