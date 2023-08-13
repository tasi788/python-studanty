def GCD(m, n):	
  if n == 0:					#終止條件
    return m 		
  return GCD(n, m % n )  	#遞迴呼叫

a, b = map(int, input().split())
print(GCD(a, b))