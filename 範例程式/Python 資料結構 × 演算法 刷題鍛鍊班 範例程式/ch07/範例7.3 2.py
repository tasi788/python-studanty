def insertion_sort(a):
  for i in range(1, len(a)):
    up = a[i]
    j = i
    while j>0 and a[j-1]>up:
      a[j] = a[j-1]
      j -= 1
    a[j] = up
        
data = [37,41,19,81,41,25,56,61,49]
insertion_sort(data)
print(data)