# Implement a queue class using two stacks. A queue is a data structure that supports the FIFO protocol (First in = first out).
# Your class should support the enqueue and dequeue methods like a standard queue.
# Here's a starting point:

from copy import deepcopy


class Queue:
    def __init__(self):
        # Fill this in.
        self.stack1 = []
        self.stack2 = []
        self.dequeue_i = 0

    def enqueue(self, val):
        # Fill this in.
        self.stack1.append(val)

    def dequeue(self):
        # Fill this in.
        self.stack2 = deepcopy(self.stack1)

        if self.stack2:
            dequeued_item = self.stack2[self.dequeue_i]
            self.stack2 = self.stack2[self.dequeue_i:]
            self.dequeue_i += 1
            return dequeued_item


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3 4



