from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        self.buckets = [None] * size
        self.size = size

    def get(self, key):
        for bucket in self.buckets:
            key_value = self.contains(key)
            if bucket:
                if key_value:
                    current = bucket.head
                    while current:
                        if key == current.value[0]:
                            return current.value[1]
                        current = current.next
        return None

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            bucket = LinkedList()
            self.buckets[index] = bucket

        key_value_pair = (key, value)
        bucket.insert(key_value_pair)

    def contains(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            return False

        current = bucket.head
        while current:
            key_value_pair = current.value
            if key_value_pair[0] == key:
                return True
            current = current.next

        return False

    def keys(self):
        gathered_keys = []
        for bucket in self.buckets:
            if bucket:
                current = bucket.head
                while current:
                    gathered_keys.append(current.value[0])
                    current = current.next
        return gathered_keys

    def hash(self, key):
        ascii_values = [ord(char) for char in key]
        ascii_sum = sum(ascii_values)

        primed = ascii_sum * 599
        index = primed % self.size

        return index
