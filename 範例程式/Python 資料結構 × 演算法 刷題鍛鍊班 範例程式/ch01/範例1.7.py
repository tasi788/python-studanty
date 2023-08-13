n = int(input())
result = 0
for i in range(1, n+1): # 定義 i 的範圍從 1 到 n
  for j in range(i+1, n+1): # 注意：j 的範圍是從 i+1 到 n
    result = result + 1
print(result)