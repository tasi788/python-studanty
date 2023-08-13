def arrayDelete(arr, k):
  for i in range(k, len(arr)-1):		# k <= i < n-1
	  arr[i] = arr[i+1] 				# i+1在右、i在左，亦即由右往左移
  arr[-1] = None					#最後一個位置填None

A = [5, 11, 25, 36, 49, 56, 77, 120]
arrayDelete(A, 3)
print(A)