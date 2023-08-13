def merge_sort(a):
  b = [0]*len(a)
  size = 1
  while size < len(a):
    for i in range(0, len(a), 2*size):
      merge(a,b,i,i+size-1,min(i+2*size-1,len(a)-1))
    size *= 2
def merge(a, b, left, m, right):
  if left>m or m+1 > right:
    return
  for i in range(left, m+1):
    b[i] = a[i]
  for j in range(m+1, right+1):
    b[j] = a[right-(j-(m+1))]
  i = left
  j = right
  for k in range(right-left+1):
    if b[i]<=b[j]:
      a[left+k] = b[i]
      i += 1
    else:
      a[left+k] = b[j]
      j -= 1
  
a1 = list(map(int, input().split()))
merge_sort(a1)
print(a1)