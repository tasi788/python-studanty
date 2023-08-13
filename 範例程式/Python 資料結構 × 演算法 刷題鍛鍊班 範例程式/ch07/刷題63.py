def merge1(a, b):
  c = [0]*(len(a)+len(b))	#目標陣列
  i = j = k = 0
  while i<len(a) and j<len(b):	
    if a[i]<=b[j]:# a[i]與b[i]小者複製到c[k]
      c[k] = a[i]
      i += 1
    else:
      c[k] = b[j]
      j += 1
    k += 1
  while i < len(a):
    c[k] = a[i]
    i += 1
    k += 1
  while j < len(b):
    c[k] = b[j]
    j += 1
    k += 1
  return c
def merge2(a, b):
  c = [0]*(len(a)+len(b))	#目標陣列
  a.append(float('inf'))		#在陣列尾端附加極大數值
  b.append(float('inf'))
  i = 0
  j = 0
  for k in range(len(c)):	# a[i]與b[i]小者複製到c[k]
    if a[i]<=b[j]:
      c[k] = a[i]
      i += 1
    else:
      c[k] = b[j]
      j += 1
  return c
  
a1 = list(map(int, input().split()))
b1 = list(map(int, input().split()))
print(merge1(a1, b1))
print(merge2(a1, b1))

#輸入範例
#1 3 8
#2 5 9 10
#輸出  1 2 3 5 8 9 10