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

def twoSum3(nums, k):
  pos = {}
  for i in range(len(nums)):
    pos[nums[i]] = i # key:value 為數值:位置，如 -3:1
  for num in nums:
    if k-num in pos:
      return pos[num], pos[k-num] # 查表取得 num 及 k-num 的位置
      
nums = [2,-3, 7, 11,15, 17]
k = int(input())				
i, j = twoSum3(nums, k)
print(i, j)