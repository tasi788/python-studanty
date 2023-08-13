def Fib_DP(n):
  A = [0]*(n+1)					# index: 0~n
  A[1] = 1
  for i in range(2, n+1):			# 2  i < n+1
    A[i] = A[i-2] + A[i-1]
  return A[n]

n = int(input())
print(Fib_DP(n))