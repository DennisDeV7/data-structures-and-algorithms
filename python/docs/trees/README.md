# Trees
Learning about binary trees and binary search

## Challenge
The challenge is to create a binary tree class and a binary search tree class
which is able to instantiate a tree, add nodes to the left and right,
and can successfully return a collection from a preorder traversal, inorder traversal
and a postorder traversal

## Approach & Efficiency
We took a recursive approach, creating a walk method inside the other methods
enabling the user to navigate through the tree

Time: O(log(n)): The time efficiency is log(n) because the time required is based
off of the height of the tree and is increasingly efficient as the size of the tree
data increases

Space: O(log(n)): The space efficiency is also log(n) because the space required
also is dependent only on the height of the tree.

## API
class BinarySearchTree(BinaryTree):\
    """\
    Takes in a binary tree in order to access pre-order, post-order,
    and in-order functions. These functions are used to return a collection
    that corresponds to the order\
    """\
    def __init__(self): --> initializes the class values\
    def add(self, value):\
        """wrap value in a Node and add it to the correct spot"""\
        def walk(root, node_to_add):\
    def contains(self, target): ---> Checking to see if the file contains what is searched for\
        def walk(root):
