'''
A circular queue is an extended version of a linear queue as it follows the First In First Out principle with the exception that it connects the last node of a queue to its first by forming a circular link. Hence, it is also called a Ring Buffer.

Circular queues make efficient use of available space by allowing the rear pointer to wrap around to the front when the end of the array is reached. This ensures no space is wasted, unlike in a linear queue where space can be left unused after elements are dequeued.
'''
class circularQ:
    def __init__(self, n):      # n = size
        self.n = n
        self.array = [None] * self.n
        self.front = 0
        self.rear = 0
        self.size = 0

    def enque(self, data):
        if self.size >= self.n:
            raise Exception("Queue is full.")
        self.array[self.rear] = data
        self.rear = (self.rear + 1) % self.n
        self.size += 1
        return self

    def deque(self):
        if self.size == 0:
            raise Exception("Underflow condition is detected.")
        temp = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.n
        self.size -= 1
        return temp

obj1 =circularQ(5)
obj1.enque(8)
obj1.enque(103)
print(obj1.deque())
obj1.enque(36)
obj1.enque(87)
print(obj1.deque())
obj1.enque(65)
print(obj1.deque())