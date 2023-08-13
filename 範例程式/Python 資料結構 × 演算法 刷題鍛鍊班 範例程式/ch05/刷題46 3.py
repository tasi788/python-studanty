from WtGraphClass import *
from queue import PriorityQueue
from stackClass import *
def Dijkstra(g, vs, vd):
  dist = [float('inf')]*g.n  #距離
  dist[vs] = 0
  prev = [None] * g.n
  decided = []
  pq = PriorityQueue()
  pq.put((0, vs))
  while not pq.empty():
    d, vx = pq.get()  #取出未定點中距離d最小者vx
    decided.append(vx)        #設vx為已定點
    if vx == vd:
      break
    for i in range(len(g.L[vx])):    
      vt = g.L[vx][i][0]        #vx的每個鄰點vt
      w = g.L[vx][i][1]        #(vx,vt)的加權
      if vt not in decided:    #vt需為未定點
        if dist[vx]+ w < dist[vt]:
          dist[vt] = dist[vx] + w
          pq.put((dist[vt], vt))
          prev[vt] = vx
  tracePath(prev, vs, vd)
  return dist[vd]
def tracePath(prev, src, dest):
  path = Stack()
  print(f'vs:{src}, vd:{dest}')
  path.push(dest)
  v = prev[dest]
  path.push(v)
  while v :
    v = prev[v]
    path.push(v)
  while not path.isEmpty():
    print(path.pop(), end = ' ')
  print()
    
g2 = WtGraph()
g2.readFile('wtGraph5-23.txt')
g2.print()
print(Dijkstra(g2, 0, 6))