def	timesTable():
  for r in range(1,10):				# 1 <= r < 10
    for c in range(1,10):			# 1 <= c < 10
	    print("%1dX%1d=%2d" %(r, c, r*c), end=" ")
    print()										#換列，給下一個r

timesTable()	