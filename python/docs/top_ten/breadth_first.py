from data_structures.binary_search_tree import BinarySearchTree
from data_structures.queue import Queue

tree = BinarySearchTree()
values=[10,5,20,7,12]
for value in values:
    tree.add(value)

def breadth_first_search(tree):
    if tree.root is None:
        return 0

    node_sum = 0
    breadth = Queue()
    breadth.enqueue(tree.root)
    while not breadth.is_empty():
        front = breadth.dequeue()
        node_sum += front.value
        print(front.value)
        if front.left:
            breadth.enqueue(front.left)
        if front.right:
            breadth.enqueue(front.right)

    return node_sum

result = breadth_first_search(tree)

print(result)
