from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        # self.push = Stack.push(value)
        # self.pop = Stack.pop(value)
        # self.peek = Stack.peek(value)
        # self.stack1 = self.push(20)
        self.top = None
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_rear = Stack.push(self, value)
        if not self.rear:
            self.rear = new_rear
            self.front = new_rear
        else:
            old_rear = self.rear
            self.rear = new_rear
            old_rear.next_ = new_rear

    def dequeue(self):
        # if self.is_empty():
        #     raise InvalidOperationError("Method not allowed on empty Queue")
        old_front = self.front
        self.front = self.front.next_
        return old_front.value

