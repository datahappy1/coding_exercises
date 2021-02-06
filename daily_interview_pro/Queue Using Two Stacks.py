# Implement a queue class using two stacks. A queue is a data structure that supports the FIFO protocol (First in = first out).
# Your class should support the enqueue and dequeue methods like a standard queue.
# Here's a starting point:

class Queue:
    def __init__(self):
        # Fill this in.
        self.stack = []

    def enqueue(self, val):
        # Fill this in.
        self.stack.append(val)

    def dequeue(self):
        # Fill this in.
        _dequeued_item = self.stack[0]
        self.stack.pop(0)
        return _dequeued_item


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
