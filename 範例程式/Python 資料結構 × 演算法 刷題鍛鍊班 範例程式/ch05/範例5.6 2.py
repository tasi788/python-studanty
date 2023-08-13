from queueClass import *
from graphList import *
def TopSort(g):
  candidate = Queue()
  indegree = [0] * g.n
  visited = [False] * g.n
  for u in range(len(g.L)):
    for v in g.L[u]:
      indegree[v] += 1
  for u in range(len(indegree)):
    if indegree[u] == 0:
      candidate.enQueue(u)
  while not all(visited):
    if candidate.isEmpty():
      return False
    u = candidate.deQueue()
    print(u, end = ' ')
    visited[u] = True
    for v in g.L[u]:
      indegree[v] -= 1
      if indegree[v] == 0:
        candidate.enQueue(v)
  return True

g1 = GraphList()
g1.readFile("graph5-26.txt")
g1.print()
if not TopSort(g1):
  print("Cycle found!")