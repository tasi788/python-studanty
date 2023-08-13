from math import floor, log					#要使用數學函式floor, log
def	palindrome(n):
  digits = floor(log(n,10))+1		#計算n的總位數
  d = digits // 2						#計算迴圈重複次數
  for _ in range(d):
    low = n % 10						#取得最低位數字
    high = n // 10**(digits-1) 	#取得最高位數字
    if low != high:
      return False
    n = n % 10**(digits-1)		#去掉最高位數字
    n = n // 10						#去掉最低位數字
    digits -= 2						#總位數少2
  return True

n = int(input())
print(palindrome(n))	