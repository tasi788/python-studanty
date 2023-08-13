n = int(input())
sum = count = 0
for i in range(1, n+1): # 定義 i 的範圍從 1 到 n
  for j in range(1, n): # 定義 j 的範圍從 1 到 n-1
    count = count + 1
    sum = sum + i
print(sum)