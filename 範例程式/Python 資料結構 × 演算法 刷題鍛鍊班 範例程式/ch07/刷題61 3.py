nums = list(map(int, input().split()))
count = {}
for num in nums:
  count[num] = count.get(num,0)+1
nums.sort(key = lambda num: count[num])
print(nums)