def FastExp(x, n):	
  if n == 1:					#終止條件
    return x 		
  half = FastExp(x, n // 2 )  	#遞迴呼叫，取得xn/2
  if (n % 2) == 1:				# n是奇數：xn = xn/2 * xn/2 * x
    return half * half * x		
  return half * half
  
x = float(input())
n = int(input())
print(FastExp(x,n))