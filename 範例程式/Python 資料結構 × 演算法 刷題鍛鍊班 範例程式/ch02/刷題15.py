def maxSubArr(nums):
  max_sum = float('-inf')
  cur_sum = 0
  for i in range(len(nums)):
	  cur_sum += nums[i]
	  max_sum = max(cur_sum, max_sum)
	  cur_sum = max(0, cur_sum)
  return max_sum
  
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArr(nums))