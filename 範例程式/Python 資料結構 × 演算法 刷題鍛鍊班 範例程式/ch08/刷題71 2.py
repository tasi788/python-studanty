def twoThree(nums1, nums2, nums3):
  count = {}
  setAll = set(nums1) | set(nums2) | set(nums3)
  for num in setAll:
    if num in nums1:
      count[num] = count.get(num,0)+1
    if num in nums2:
      count[num] = count.get(num,0)+1
    if num in nums3:
      count[num] = count.get(num,0)+1
  result = []
  for num in count:
    if count[num]>= 2:
      result.append(num)
  return result
  
a1 = [1, 1, 31, 20]
a2 = [20, 31, 3]
a3 = [31]
print(twoThree(a1, a2, a3))
#輸出：[20, 31]