from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree1, tree2):
    common = []
    common_hash = Hashtable()

    for value in tree1.pre_order():
        common_hash.set(value, value)

    for value in tree2.pre_order():
        if common_hash.contains(value):
            if value not in common:
                common.append(value)
    return common
