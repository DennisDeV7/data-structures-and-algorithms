from data_structures.hashtable import Hashtable
import re

def first_repeated_word(book):
    book_text = book.lower().split()
    library = Hashtable()
    for expression in book_text:
        word = re.sub(r'[^a-zA-Z]+', "", expression)
        if library.contains(word):
            return library.get(word)
        library.set(word, word)
    return None

