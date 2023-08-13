def partition(a, left, right):
  i = left + 1
  j = right
  pivot = a[left]
  while True:
    while i<=right and a[i]<= pivot:
      i += 1
    while j>left and a[j]>= pivot:
      j -= 1
    if i > j: break
    a[i], a[j] = a[j], a[i]
  a[left], a[j] = a[j], a[left]
  return j
a1 = list(map(int, input().split()))
print(partition(a1, 0, len(a1)-1))
print()
print(a1)