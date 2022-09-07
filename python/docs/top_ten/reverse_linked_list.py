from data_structures.linked_list import LinkedList

def reverse_linked_list(linked):
    # def reverse_node(head):

    previous = None
    current = linked.head

    while current:
        upcoming = current.next
        current.next = previous
        previous = current
        current = upcoming

    # return previous
    linked.head = previous
    return linked

values = ["a", "b", "c", "d", "e"]
letters = LinkedList

for value in values:
    letters.insert(value)


