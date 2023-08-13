def distribute(a, m=10):
  count = [0]*m
  b = [0]*len(a)
  for i in range(len(a)):		#計數
    count[ a[i] ] += 1
  for j in range(1, m):		#累積
    count[j] +=  count[j-1]
  for i in range(len(a)-1, -1, -1):		#分配
    b[count[ a[i] ]-1] = a[i]
    count[ a[i] ] -= 1
  for i in range(len(a)):		#回抄至a[]
    a[i] = b[i]

nums = list(map(int, input().split()))
distribute(nums, 3)  # 0~2 共3種可能
print(nums)