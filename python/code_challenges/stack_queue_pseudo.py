from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        self.in_queue = Stack()
        self.out_queue = Stack()

    def enqueue(self, val):
        while self.out_queue.top:
            self.in_queue.push(self.out_queue.pop())
        self.in_queue.push(val)

    def dequeue(self):
        while self.in_queue.top:
            self.out_queue.push(self.in_queue.pop())
        return self.out_queue.pop()

