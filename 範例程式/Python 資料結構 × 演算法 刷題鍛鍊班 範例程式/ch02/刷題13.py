def backPacking(argItems, argW):
  i = total_p = 0
  left_w = argW
  while i<len(argItems) and left_w>0:
    if argItems[i][2]<=left_w:
      total_p += argItems[i][3]
      left_w -= argItems[i][2]
    else:
      total_p += argItems[i][0]*left_w
      left_w = 0
    i += 1
  return total_p

W_limit = int(input())
N = int(input())  
items = [ [ ] for _ in range(N)]
name = input().split()
W = list(map(int, input().split()))
P = list(map(int, input().split()))
for i in range(N):
  items[i] = [P[i]/W[i],name[i],W[i],P[i]]
items.sort(reverse=True)  
print(backPacking(items, W_limit))
#輸入範例
#30
#3
#A  B  C
#5  10  20
#50  60  140
#輸出 220