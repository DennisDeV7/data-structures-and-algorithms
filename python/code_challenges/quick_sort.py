def quick_sort(nums, left, right):
  """
  nums: an unsorted list
  left: starting index of list, (0)
  right: ending index of list, len(list) - 1
  """
  if left < right:
    position = partition(nums, left, right)

    quick_sort(nums, left, position - 1)
    quick_sort(nums, position + 1, right)



def partition(nums, left, right):
  pivot = nums[right]
  low = left - 1

  for i in range(left, right):
    if nums[i] <= pivot:
      low += 1
      swap(nums, i, low)

  swap(nums, right, low + 1)

  return low + 1


def swap(nums, i, low):
  temp = nums[i]
  nums[i] = nums[low]
  nums[low] = temp


if __name__ == "__main__":
  test = [8,4,23,42,16,15]

  quick_sort(test, 0, len(test)-1)

  print(test)
