from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # if no rear then new_rear is the rear
        # create new node named new_rear
        # assign current rear to new_rear
        # set self.rear to new_rear
        # set old_rear's next to new_rear
        new_rear = Node(value)
        if not self.rear:
            self.rear = new_rear
            self.front = new_rear
        else:
            old_rear = self.rear
            self.rear = new_rear
            old_rear.next_ = new_rear

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("InvalidOperationError")
        return self.front.value

    def is_empty(self):
        return self.front is None

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty Queue")
        # remove from front
        # reset front ot the 2nd in line
        # return the value
        old_front = self.front
        self.front = self.front.next_
        return old_front.value

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_
