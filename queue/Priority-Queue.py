'''
a priority queue is an abstract data type similar to a regular queue or stack abstract data type. Each element in a priority queue has an associated priority. In a priority queue, elements with high priority are served before elements with low priority. In some implementations, if two elements have the same priority, they are served in the same order in which they were enqueued. In other implementations, the order of elements with the same priority is undefined.
'''

# q = []
# q.append(10)
# q.append(300)
# q.append(180)
# q.append(100)
# q.append(150)
# print(q)

# # Let assume that the value with less have the most priority
# q.sort()
# print("Sorted queue=",q)

# print(q.pop(0)) # 10 removed
# print(q.pop(0))
# print(q.pop(0))
# print(q.pop(0))
# print(q.pop(0))


import queue
q1 = queue.PriorityQueue()
q1.put(10)
q1.put(200)
q1.put(130)
q1.put(70)
print(q1)
print(q1.get())
print(q1.get())
print(q1.get())
print(q1.get())

