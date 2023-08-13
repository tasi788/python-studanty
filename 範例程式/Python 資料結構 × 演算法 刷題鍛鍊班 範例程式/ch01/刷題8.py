def hanoi(n, source, by, to):
  if n > 0:
    hanoi(n-1, source, to, by)
    print("{} : {} -> {}".format(n, source, to))
    hanoi(n-1, by, source, to)

n = int(input())
hanoi(n, 'A', 'B', 'C')