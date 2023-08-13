def findMax(arr):
  max_now = arr[0]
  for i in range(1, len(arr)):				# 1  i < n
	  max_now = max(max_now, arr[i]) 	# 輪流挑戰
  return max_now					# 最後勝者

def findMaxPos(arr):
  max_now = 0					# 第0個位置的資料先當霸主
  for i in range(1, len(arr)):
    if arr[i] > arr[max_now]:		
      max_now = i
  return max_now					# 最後勝者

A = [5, 11, 25, 336, 49, 256, 77, 120]
print(findMax(A))
print(f"最大的元素在：{findMaxPos(A)}")
