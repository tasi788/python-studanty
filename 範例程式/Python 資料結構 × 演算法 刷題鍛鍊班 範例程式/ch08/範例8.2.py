def interSearch(a, key):
  left, r = 0, len(a)-1
  while left <= r:
    if a[r]==a[left]:
      x = 1
    else:
      x = min(1,(key-a[left])/(a[r]-a[left]))
    m = int(left+ x*(r-left))
    if a[m] == key:
      return m
    elif a[m] < key:
      left = m+1
    else:
      r = m-1
  return -1

nums = [6, 33, 39, 41, 52, 55, 69, 77, 78, 81]
print(interSearch(nums, 6))
print(interSearch(nums, 77))
print(interSearch(nums, 90))