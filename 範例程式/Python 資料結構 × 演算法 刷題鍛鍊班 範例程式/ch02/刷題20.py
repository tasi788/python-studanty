def checkRecord(s) :
  abs = count = max_count = 0
  for x in s:						#第一次掃描
    if x == 'L':
      count += 1 
      max_count = max(max_count, count)
    else:
      count = 0					#連續L的次數歸零
      if x == 'A':
        abs+=1
  if abs < 2 and max_count < 3:	#根據條件判斷是否得獎
    return True
  return False

s = input().upper()
print(checkRecord(s))
