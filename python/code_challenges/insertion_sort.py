
def insertion_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        key = unsorted_list[i]

        j = i -1
        while j >= 0 and key < unsorted_list[j]:
            unsorted_list[j+1] = unsorted_list[j]
            j -= 1
        unsorted_list[j+1] = key

test_list = [8, 4, 23, 42, 16, 15]
insertion_sort(test_list)
print(test_list)
