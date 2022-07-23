from multiprocessing.sharedctypes import Value


class LinkedList:
    """
    Put docstring here
    """
    string = ""
    def __init__(self):
        # initialization here
        self.head = None

    def __str__(self):
        some = LinkedList.to_string(self)
        if self.head == None:
            return "NULL"
        else:
            return some


    def insert(self, value):
        # method body here
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        LinkedList.string = ""

    def to_string(self):
        current = self.head
        while current:
            LinkedList.string += str("{ " + f"{ current.value }" + " }")
            if current.next != "NULL":
                LinkedList.string += " -> "
            if current.value == None:
                LinkedList.string += "NULL"
            if current.next == None:
                LinkedList.string += "NULL"
            current = current.next
        return LinkedList.string

    def includes(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False


class Node:
    """
    docstring
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        greeting = f"{self.value}"
        return greeting

    def __repr__(self):
        declaration = f"{self.value}"
        return declaration

class TargetError:
    pass



if __name__ == "__main__":
    nums = LinkedList()
    nums.insert("apple")
    print(nums)
    nums.insert("banana")
    print(nums)
