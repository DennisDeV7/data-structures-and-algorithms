# Hashtables

This challenge involved creating a hashtable and appropriate tests

## Challenge

Create a Hash table by creating the following methods: set(), get(), contains(), keys(), and hash()

## Approach & Efficiency

Time efficiency: O(n): since this implementation still has to iterate through all of the keys in order to find the correct one it is a linear relationship
Space efficiency: O(n): as the size of the dictionary increases, so does the space requirement in a linear relationship

## API

set(): puts the key value pairs in the dictionary by calling hash() and using a LinkedList

get(): returns the value associated with the given key by looping through the dictionary and traversing each linked list to see if the value is there and returning it, if it is.

contains(): Loops through the dictionary and traverses each linked list, looking for a key that matches a given key. If it is found, return True, else return False.

keys(): Loops and traverses just like get() and contains() except it appends all of the keys to a list and returns the list

hash(): This function creates the hash value that is associates with the key

[code](../../data_structures/hashtable.py)

[tests](../../tests/data_structures/test_hashtable.py)
