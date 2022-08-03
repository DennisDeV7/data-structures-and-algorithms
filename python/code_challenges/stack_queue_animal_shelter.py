from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.in_queue = Queue()
        self.out_queue = Queue()

    def enqueue(self, animal):
        # while self.out_queue.rear:
        #     self.in_queue.enqueue(self.out_queue.dequeue())
        self.in_queue.enqueue(animal)


    def dequeue(self, pref):
        # while self.in_queue.rear:
        #     self.out_queue.enqueue(self.in_queue.dequeue())
        return self.out_queue.dequeue()


class Dog:
    pass


class Cat:
    pass
