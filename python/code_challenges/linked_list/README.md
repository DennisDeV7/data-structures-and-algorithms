# Linked List

Linked list is a challenge to learn about linked lists in python. The goal of the challenge is to be able to insert nodes into the list and navigate through the list in order to print a string representing the chain of nodes and to test if a value is inside the node.

## Challenge

In addition to the above description, the specific tasks were outlined in the tests that needed to pass as follows:

- [x] Can successfully instantiate an empty linked list
- [x] Can properly insert into the linked list
- [x] The head property will properly point to the first node in the linked list
- [x] Can properly insert multiple nodes into the linked list
- [x] Will return true when finding a value within the linked list that exists
- [x] Will return false when searching for a value in the linked list that does not exist
- [x] Can properly return a collection of all the values that exist in the linked list

## Approach & Efficiency

I took the approach of takling each test (nine in total) one at a time. I made all functions iterative because I think that was the only way to navigate through the linked chain for the time being.

This function is linear in relation to time and space efficiency (O(n)). The time and space requirement increase with respect to the size of the input array

## API

### LinkedList

- def __init__(self): Initializes the class with head attribute
- def __str__(self): Will return one of the two strings needed "NULL" or the list of nodes
- def insert(self, value): Function that inserts a node into the linked list
- def to_string(self): Function that navigates through the linked list and converts the output into a string such as `{ apple } -> { banana } -> NULL`
- def includes(self, value): Function that will navigate throught he linked list to see if a given value is in it

### Node

def __init__(self, value, next=None): Initializes the Node class with value and next attributes
