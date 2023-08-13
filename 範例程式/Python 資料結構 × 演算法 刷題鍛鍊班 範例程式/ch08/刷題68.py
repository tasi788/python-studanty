def binSearch2(a, key):
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
  return left

nums = [6, 33, 39, 41, 52, 55, 69, 77, 78, 81]
print(binSearch2(nums, 5))
print(binSearch2(nums, 33))
print(binSearch2(nums, 42))
print(binSearch2(nums, 90))