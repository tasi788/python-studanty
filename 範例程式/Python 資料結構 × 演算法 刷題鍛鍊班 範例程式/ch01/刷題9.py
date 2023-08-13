def Fib(n):
  if n == 0: return 0			#終止條件1
  if n == 1: return 1			#終止條件2
  return Fib(n-1) + Fib(n-2)	#兩個遞迴呼叫
def iterativeFib(n):
  if n == 0: return 0			#底層1
  if n == 1: return 1			#底層2
  Fn_1, Fn_2 = 1, 0
  for i in range(2, n+1):  		# 2  i < n+1
    Fn = Fn_1 + Fn_2		# 生成Fib(i)
    Fn_2 = Fn_1
    Fn_1 = Fn
  return Fn 
n = int(input())
print(Fib(n))
print(iterativeFib(n))