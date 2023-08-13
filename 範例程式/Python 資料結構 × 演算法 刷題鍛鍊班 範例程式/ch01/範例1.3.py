def sum(n):
  if n==2:
    return 2                  # 終止條件
  return sum(n-1) + (n-1)*n   # 遞迴呼叫

def sum2(n):
  sum = 0
  for i in range(1, n):
    sum += i*(i+1)
  return sum

n = int(input())
print(sum(n))
print(sum2(n))