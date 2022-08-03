from data_structures.queue import Queue


class AnimalShelter:

    def __init__(self):
        self.dog = Queue()
        self.cat = Queue()

    def enqueue(self, animal):
        if animal.breed == "dog":
            self.dog.enqueue(animal)

        if animal.breed == "cat":
            self.cat.enqueue(animal)

    def dequeue(self, pref):
        if pref == "dog":
            return self.dog.dequeue()

        if pref == "cat":
            return self.cat.dequeue()


class Dog:

    def __init__(self):
        self.breed = "dog"


class Cat:

    def __init__(self):
        self.breed = "cat"
