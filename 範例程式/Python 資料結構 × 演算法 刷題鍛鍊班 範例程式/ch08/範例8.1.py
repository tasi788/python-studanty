def seqSearch(a, key):
  for i in range(len(a)):
    if a[i] == key:
      return i
  return -1

nums = [39, 81, 6, 78, 69, 41, 52, 33, 55, 77]
print(seqSearch(nums, 6))
print(seqSearch(nums, 33))
print(seqSearch(nums, 90))