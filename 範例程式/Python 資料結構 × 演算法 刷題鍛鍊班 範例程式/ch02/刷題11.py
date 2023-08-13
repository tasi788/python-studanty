def twoSum(nums, k):
  for i in range(len(nums)):				
    for j in range(i+1, len(nums)):		
      if nums[i] + nums[j] == k:
        return nums[i], nums[j]
nums = [2,-3, 7, 11,15, 17]
k = int(input())				
i, j = twoSum(nums, k)
print(i, j)