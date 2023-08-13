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

def twoSum2(nums, k):
  valuePos = []
  for i in range(len(nums)):
    valuePos.append([nums[i],i]) 
  valuePos.sort()
  nums.sort()
  for i in range(len(nums)):
    j = binSearch(nums, k-nums[i])
    if j != -1:
      return valuePos[i][1], valuePos[j][1]
      
nums = [2,-3, 7, 11,15, 17]
k = int(input())				
i, j = twoSum2(nums, k)
print(i, j)