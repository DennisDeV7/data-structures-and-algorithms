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
        LinkedList.string = ""
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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        LinkedList.string = ""

    def insert_before(self, d_node, value):
        new_node = Node(value)
        current = self.head
        if current is None:
            raise TargetError

        if current.value == d_node:
            new_node.next = self.head
            self.head = new_node

        while current.next is not None:
            if current.next.value == d_node:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next
        LinkedList.string = ""
        raise TargetError

    def insert_after(self, target, value):
        new_node = Node(value)
        current = self.head
        if target is None:
            print("Not in list")
            return
        else:
            while current:
                if current.value == target:
                    new_node.next = current.next
                    current.next = new_node
                    return
                else:
                    current = current.next
        LinkedList.string = ""



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

class TargetError(Exception):
    pass



if __name__ == "__main__":
    nums = LinkedList()
    nums.insert("apple")
    print(nums)
    nums.insert("banana")
    print(nums)
    nums.insert_after("banana", "cucumber")
    print(nums)
