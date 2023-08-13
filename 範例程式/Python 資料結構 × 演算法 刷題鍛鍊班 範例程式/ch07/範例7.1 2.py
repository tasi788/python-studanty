def bubble_sort(a):
  for i in range(len(a)-1, 0, -1):
    for j in range(1, i+1):
      if a[j-1]>a[j]:
        a[j-1], a[j] = a[j], a[j-1]

def bubble_sort2(a):
  for i in range(len(a)-1, 0, -1):
    swapFlag = False
    for j in range(1, i+1):
      if a[j-1]>a[j]:
        a[j-1], a[j] = a[j], a[j-1]
        swapFlag = True
    if not swapFlag:
      return
        
data = [37,41,19,81,41,25,56,61,49]
bubble_sort(data)
print(data)