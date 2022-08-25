# Blog Notes: Quick Sort

In this blog post we talk about the steps required to create an merge sort function.

## Pseudocode

```txt
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

## Trace

Start with [8,4,23,42,16,15]

Upon the first pass, the last value in the list, `15`, is made the pivot point. It will then analyze the list and put everything that is lower than the pivot on the left and everything that is higher remains on the right. Each value that is lower than the pivot is placed in the left side by swapping it with the first value of the list. If there are still values on the right, then the pivot is moved to the next position after the values that were lower than it.

Example for first pass:

[8,4,23,42,16,15]  Pivot = 15

Start at `8`

is `8` less than `15`? yes\
swap `8` with the first value (it's already there)

result: [8,4,23,42,16,15]

Look at `4`

is `4` less than `15`? yes\
swap `4` with the first value

result: [4,8,23,42,16,15]

Look at `23`

is `23` less than `15`? no\
stay

no change

Look at `42`

is `42` less than `15`? no\
stay

no change

Look at `16`

is `16` less than `15`? no\
stay

We do not include 15 in the iteration. Now that it reached the pivot value we swap it with the first value after the "left"

result: [4,8,15,23,42,16]

## Time Complexity

time: O(nlogn): the recursive function is logarithmic by the constant splitting of the list.
space: O(1): The space requirement is constant because the list is sorted in place.

[Code](python/code_challenges/quick_sort.py)
