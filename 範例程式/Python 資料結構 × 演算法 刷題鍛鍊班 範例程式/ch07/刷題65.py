def evenOdd(a):
  i = 0
  j = len(a)-1
  while True:
    while i<= len(a)-1 and a[i]%2 == 0 :
      i += 1
    while j>=0 and a[j]%2 :
      j -= 1
    if i > j: break
    a[i], a[j] = a[j], a[i]
  
a1 = list(map(int, input().split()))
evenOdd(a1)
print(a1)