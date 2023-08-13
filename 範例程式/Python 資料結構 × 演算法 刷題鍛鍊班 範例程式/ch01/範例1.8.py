n = int(input())
result = 0
for i in range(1, n+1): # 定義 i 的範圍從 1 到 n
  for j in range(i, n+1): # j 的範圍是從 i 到 n
    for k in range(j, n+1): # k 的範圍是從 j 到 n
      result = result + 1
print(result)