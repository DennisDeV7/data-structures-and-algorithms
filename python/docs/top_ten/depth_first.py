import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from data_structures.binary_search_tree import BinarySearchTree

tree = BinarySearchTree(values=[10,5,20,7,12])

def depth_first_search(tree):
    def walk(root):
        if root is None:
            return
        print(root.value)
        walk(root.left)
        walk(root.right)


    walk(tree.root)

depth_first_search(tree)
