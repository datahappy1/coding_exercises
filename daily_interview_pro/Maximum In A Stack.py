# Implement a class for a stack that supports all the regular functions (push, pop)
# and an additional function of max() which returns the maximum element in the stack
# (return None if the stack is empty). Each method should run in constant time.

class MaxStack:
    def __init__(self):
        # Fill this in.
        self.stack = []
        self.trackStack = []

    def push(self, val):
        # Fill this in.
        self.stack.append(val)
        if len(self.stack) == 1:
            self.trackStack.append(val)
            return
        # If current element is greater than
        # the top element of track stack,
        # append the current element to track
        # stack otherwise append the element
        # at top of track stack again into it.
        if val > self.trackStack[-1]:
            self.trackStack.append(val)
        else:
            self.trackStack.append(self.trackStack[-1])
        # print(f'x {len(self.trackStack)}')

    def pop(self):
        # Fill this in.
        self.stack.pop()
        self.trackStack.pop()

    def max(self):
        # Fill this in.
        if self.stack:
            return self.trackStack[-1]
        return None


from datetime import datetime

s = MaxStack()
# for _ in range(0, 10000000):
#     s.push(_)

start = datetime.now()

s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2

print(datetime.now() - start)
