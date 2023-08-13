def arrayInsert(arr, k, value):
  for i in range(len(arr)-1, k, -1):	# n-1 >= i > k，亦即k < i <= n-1
	  arr[i] = arr[i-1] 				# i-1在左、i在右，亦即由左往右移
  arr[k] = value	

A = [5, 11, 25, 36, 49, 56, 77, 120]
arrayInsert(A, 3, 27)
print(A)