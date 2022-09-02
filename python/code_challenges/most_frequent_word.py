from data_structures.hashtable import Hashtable


def find_most_frequent_word(book):
    word_list = book.split(" ")
    library = Hashtable()

    largest_index = 0
    for word in word_list:

        if library.contains(word):
            index = library.get(word)
            index_increment = index + 1
            library.set(word, index_increment)
            if index_increment > largest_index:
                largest_index = index_increment
                largest_index_word = word
        else:
            library.set(word, 1)

    return largest_index_word

if __name__ == "__main__":

    print(find_most_frequent_word("In a galaxy far far away"))

    print(find_most_frequent_word("No Try not Do or do not There is no try"))

    print(find_most_frequent_word("which which which one one will print print print print"))
