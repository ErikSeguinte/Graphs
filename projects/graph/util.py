from collections import deque

# Note: This Queue class is sub-optimal. Why?
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def multi_enqueue(self, values):
        self.queue.extend(values)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.popleft()
        else:
            return None

    def size(self):
        return len(self.queue)

    def __len__(self):
        return self.size()


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def multi_push(self, values):
        self.stack.extend(values)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

    def __len__(self):
        return self.size()
