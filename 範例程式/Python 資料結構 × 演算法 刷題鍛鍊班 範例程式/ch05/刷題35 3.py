from graphList import *
def isStar(g):
  num_star = num_other = 0
  for v in g.L:
    if len(v) == g.n - 1:
      num_star += 1
    elif len(v) == 1:
      num_other += 1
  if g.e==2*(g.n-1) and num_star==1 and num_other==g.n-1:
    return True
  return False

g1 = GraphList()
g1.readFile("graph5-11.txt")
g1.print()
print(isStar(g1))