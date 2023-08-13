from HashTableClass import *
def twoSum4(nums, k):
  h = HashTable()
  for i in range(len(nums)):
    h.add(nums[i], i)
  for num in nums:
    value = h.get(k-num)
    if value != None:
      return h.get(num), value
      
nums = [2,-3, 7, 11,15, 17]
k = int(input())				
i, j = twoSum4(nums, k)
print(i, j)
