listA = [4,10,8,14,5]
listB = [5,6,10,8,4,5]
def findIntersec(l1:[int], l2:[int]): 
  n1, n2 = len(l1), len(l2)
  if l1[-1] != l2[-1]:
    return None
  if n1 < n2:
    l1, l2 = l2, l1
    n1, n2 = n2, n1
  diff = n1 - n2
  i, j = diff, 0
  flag = False
  start = -1
  while j<n2:
    if l1[i] == l2[j]:
      if not flag:
        start = j
      flag = True
    else:
      flag = False
    i, j = i+1, j+1
  return l2[start]
  
i = findIntersec(listA, listB)
if i != None:
  print(i)
else:
  print('No intersection')
