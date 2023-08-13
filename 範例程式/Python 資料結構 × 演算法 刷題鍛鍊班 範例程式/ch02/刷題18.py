def Pascal(n):
  P = [[1]*(n+1) for _ in range(n+1)]	# index: 1~n, 1~n (0不會用到)
  for i in range(3, n+1):			# 3 <= i < n+1
    for j in range(2, i):			# 2 <= j < i
      P[i][j] = P[i-1][j-1] + P[i-1][j]
  for i in range(1, n+1):
    for j in range(1, i+1):			
      print(P[i][j], end= ' ')
    print()
    
n = int(input())
Pascal(n)