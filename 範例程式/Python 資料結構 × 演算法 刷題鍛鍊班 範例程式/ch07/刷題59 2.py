def isLarger(a, b):  #若a>=b得True
  if str(a)+str(b) >= str(b)+str(a):
    return True
  return False
  
def largestNum(nums):
  result = ""    #結果字串
  while len(nums):  #當來源陣列還有資料時重複迴圈選出最大數
    largestPos = 0
    for j in range(1, len(nums)):  #nums[j]輪流挑戰nums[largestPos]
      if isLarger(nums[j], nums[largestPos]):
        largestPos = j    #挑戰成功，霸主換成j
    result += str(nums[largestPos])  #將最大數放入結果字串
    nums.remove(nums[largestPos])    #將最大數由來源陣列中刪除
  return result
      
nums = [41, 5, 42, 52, 7]
print(largestNum(nums))
