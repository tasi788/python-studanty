def	starTree(n):
  for r in range(1,n+1):		# 1 <= r < n+1  (範圍1~n)
    for s in range(n-r):		# 0 <= s < n-r  (共n-r次)
      print(' ', end = '')	# 印空格，不換列
    for c in range(2*r - 1):		# 0 <= c < 2*r - 1 (共2*r-1次)
	    print('*', end = '') 	# 印星號，不換列
    print()							    #換列，給下一個r

n = int(input())
starTree(n)		