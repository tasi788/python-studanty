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

def twoSum(nums, k):
  nums.sort()
  for num in nums:
    if binSearch(nums, k-num) != -1:
      return num, k-num
      
nums = [2,-3, 7, 11,15, 17]
k = int(input())				
m, n = twoSum(nums, k)
print(m, n)