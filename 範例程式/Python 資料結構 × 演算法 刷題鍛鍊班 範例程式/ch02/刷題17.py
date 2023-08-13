def C(n, k):
  if k == 0 or n == k: return 1		#終止條件
  return C(n-1, k-1) + C(n-1, k)		#兩個遞迴呼叫
def Binomial(n, k):
  A = [[1]*(k+1) for _ in range(n+1)]	# index: 0~n, 0~k
  for i in range(2, n+1):			# 2  i < n+1
    right = min(i, k+1)				# j > k的部分都不會用到
    for j in range(1, right):			# 1  j < min(i, k+1)
      A[i][j] = A[i-1][j-1] + A[i-1][j]
  return A[n][k]

n, k = map(int, input().split())
print(Binomial(n,k))
print(C(n,k))