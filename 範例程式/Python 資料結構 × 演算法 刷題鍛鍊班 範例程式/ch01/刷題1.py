def	countZero(n):
  count, max_count = 0, 0		# 初設為0
  while n > 0:
    d = n % 10				# 取得個位數字
    if d == 0:					# 個位數字為0
      count += 1				# 計數器加1
      max_count = max(max_count, count)	# max_count紀錄目前最大
    else:
      count = 0				# 個位數字不為0則計數器歸零
    n = n // 10				# 去除1位數字
  return max_count			#max_count是答案
n = int(input())
print(countZero(n))	