def merge_sort(a, b, left, right):
  if left == right: return
  m = (left+right)//2
  merge_sort(a, b, left, m)
  merge_sort(a, b, m+1, right)
  merge(a, b, left, m, right)
  
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
b1 = [0]*len(a1)
merge_sort(a1, b1, 0, len(a1)-1)
print(a1)