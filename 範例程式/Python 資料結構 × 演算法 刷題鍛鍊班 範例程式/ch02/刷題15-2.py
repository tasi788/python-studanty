def maxSubArr2(nums):
  max_sum = float('-inf')
  cur_sum = 0
  starti = max_starti = max_endi = 0
  for i in range(len(nums)):
    cur_sum += nums[i]
    if cur_sum > max_sum:
      max_sum = cur_sum
      max_starti = starti
      max_endi = i
    if cur_sum < 0:
      cur_sum = 0
      starti = i+1
  return max_sum, max_starti, max_endi
nums = [-2, 1, -3, 4, -10, 2, 10, -5, 6]
print(maxSubArr2(nums))