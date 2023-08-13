n = int(input())
sum = 0
for i in range(1, n+1): # i 的範圍是從 1 到 n
  sum = sum + i           # 也可寫成 sum += i
print(sum)