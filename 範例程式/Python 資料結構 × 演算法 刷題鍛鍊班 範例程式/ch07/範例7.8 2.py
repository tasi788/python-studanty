from math import *
def radixSort(a, m=10):
  digits = floor(log(max(a),m))+1
  count = [0]*m
  b = [0]*len(a)
  for k in range(digits):
    for i in range(m):
      count[i] = 0
    for i in range(len(a)):		#計數
      d = get_digit(a[i], k, m)
      count[d] += 1
    for j in range(1, m):		#累積
      count[j] +=  count[j-1]
    for i in range(len(a)-1, -1, -1):		#分配
      d = get_digit(a[i], k, m)
      b[count[d]-1] = a[i]
      count[d] -= 1
    for i in range(len(a)):		#回抄至a[]
      a[i] = b[i]
def get_digit(num, k, m=10):
  d = num // m**k
  d = d % m
  return d
  
a1 = list(map(int, input().split()))
radixSort(a1)
print(a1)
