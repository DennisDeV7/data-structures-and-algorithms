# Blog Notes: Merge Sort

In this blog post we talk about the steps required to create an merge sort function.

## Pseudocode

```txt
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Trace

test case: [8,4,23,42,16,15]

When merge_sort([8,4,23,42,16,15]) is called, the function will find the middle and then make a left and a right list from the middle.

left = [8,4,23]
right = [42,16,15]

Each side is continuously broken in half until it can't anymore

left = [8,4] [23]
left = [8][4] [23]

right = [42, 16] [15]
right = [42][16] [15]

Once they are broken down to singular values they are sorted and merged. This process continues throughout the call stack until the list is back to its original length.

left = [4][8] [23]
left = [4,8][23]
left = [4,8,23]

right = [16][42] [15]
right = [16, 42] [15]
right = [15, 16, 42]

[4,8,23] [15, 16, 42]

[4, 8, 15, 16, 23, 42]

## Time Complexity

time: O(nlogn): the recursive function is logarithmic by the constant splitting of the list.
space: O(1): The space requirement is constant because the list is sorted in place.

[Code](python/code_challenges/merge_sort.py)
