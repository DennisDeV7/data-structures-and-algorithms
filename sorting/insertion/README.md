# Insertion Sort

In this blog post we talk about the steps required to create an insertion sort function.

## Pseudocode

```txt
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

## Trace

```txt
test set: [8, 4, 23, 42, 16, 15]
              ^
```

In the first pass we start at index one, which is four. Since four is less than eight, eight moves up one position in the array. This results in:

pass one result: `[4, 8, 23, 42, 16, 15]`

```txt
pass two: [4, 8, 23, 42, 16, 15]
                  ^
```

In the second pass, we start at index two which is 23. Since 23 is not less than eight, the list is unchanged. The result is:

pass two result: `[4, 8, 23, 42, 16, 15]`

```txt
Pass three: [4, 8, 23, 42, 16, 15]
                        ^
```

In the third pass, we start at index three which is 42. Since 42 is not less than 23, the list is unchanged. The result is:

Pass three result: `[4, 8, 23, 42, 16, 15]`

```txt
Pass four: [4, 8, 23, 42, 16, 15]
                           ^
```

In the fourth pass, we start at index four which is 16. Since 16 is less than 42, their positions in the list are swapped resulting in `[4, 8, 23, 16, 42, 15]`. After swapping, 16 is compared to 23. Since 16 is also less than 23 they swap again resulting in `[4, 8, 16, 23, 42, 15]`. Finally, 16 is compared to 8. As 16 is greater than 8 the round stops and the result is:

Pass four result: `[4, 8, 16, 23, 42, 15]`

```txt
Pass five: [4, 8, 16, 23, 42, 15]
                               ^
```

In the fifth pass, we are finally at 15. As 15 is less than 42, they are swapped. Since 15 is less than 23, they are swapped. Next, 15 is also less then 16, so they swap. Finally 15 is not less than 8 so the loop breaks and returns:

Pass five result:  `[4, 8, 15, 16, 23, 42]`

## Efficiency

- Time: O(n^2)
      - The time complexity is exponential because the function required to loop through the entire array at times for each number. As the list size increases, the time increases by the size of the list squared.

- Space: O(1)
      - The space efficiency is constant because the function executes the sort in place and does not require additional space.
