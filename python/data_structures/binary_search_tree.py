from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    # def __init__(self):
    #     super().__init__()

    def add(self, value):
        """wrap value in a Ne and add it to the correct spot"""
        node = Node(value)
        if not self.root:
            self.root = node
            return

        def walk(root, node_to_add):
            if root is None:
                return

            if node_to_add.value < root.value:
                if not root.left:
                    # spot it open
                    root.left = node_to_add
                else:
                    walk(root.left, node_to_add)
            else:
                if not root.right:
                    # spot available
                    root.right = node_to_add
                else:
                    walk(root.right, node_to_add)
        walk(self.root, node)

    def contains(self, target):
        def walk(root):
            if root is None:
                return False

            if root.value == target:
                return True

            if target < root.value:
                return walk(root.left)
            else:
                return walk(root.right)
        return walk(self.root)
