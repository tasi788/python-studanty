def C(n, k):
  if k == 0 or n == k: return 1		#終止條件
  return C(n-1, k-1) + C(n-1, k)		#兩個遞迴呼叫
n, k = map(int, input().split())
print(C(n,k))
