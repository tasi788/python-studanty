def binSearch(a, key):
  left = 0
  r = len(a)-1
  while left <= r:
    m = (left+r)//2
    if a[m] == key:
      return m
    elif a[m] < key:
      left = m+1
    else:
      r = m-1
  return -1

nums = [6, 33, 39, 41, 52, 55, 69, 77, 78, 81]
print(binSearch(nums, 6))
print(binSearch(nums, 77))
print(binSearch(nums, 90))