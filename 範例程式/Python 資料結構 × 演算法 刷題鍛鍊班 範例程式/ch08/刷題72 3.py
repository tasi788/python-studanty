def luckyNumber(nums):
  count = {}
  for num in nums:
    count[num] = count.get(num,0)+1
  maxLucky = -1
  for num in count:
    if count[num] == num:
      maxLucky = max(maxLucky, num)
  return maxLucky
  
a = [4, 5, 1, 2, 2, 3, 3, 3]
print(luckyNumber(a))
#輸出 3 