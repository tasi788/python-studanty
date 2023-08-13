def find(Text, Pattern) :
  T = P = StartT = 0
  n = len(Text)
  m = len(Pattern)
  EndT = m-1
  while P < m and StartT <= n-m:
    if Text[T] == Pattern[P]:	
      P += 1
      T += 1
    else:
      StartT += 1
      EndT += 1
      T = StartT
      P = 0
    if P == m:
      return StartT
  return -1

Text = input()
Pattern = input()
print(find(Text, Pattern))
