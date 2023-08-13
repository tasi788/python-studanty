def selection_sort(a):
  for i in range(len(a)-1, 0, -1):
    max = 0
    for j in range(1, i+1):
      if a[j]> a[max]:
        max = j
    a[max], a[i] = a[i], a[max]
        
data = [37,41,19,81,41,25,56,61,49]
selection_sort(data)
print(data)