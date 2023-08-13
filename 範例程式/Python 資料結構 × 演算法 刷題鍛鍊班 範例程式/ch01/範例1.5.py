n = int(input())
sum = count = 0
for i in range(1, n+1): # i 的範圍是從 1 到 n
  count = count + 1 # 也可寫成 count += 1
  sum = sum + i
print(sum)