from queueClass import *
class GraphList:
  def read(self):
    self.n, self.e = map(int, input().split())
    self.L = [[] for _ in range(self.n)]
    for _ in range(self.e):
      i, j = map(int,input().split())
      self.L[i].append(j)
  def readFile(self,fileName):
    fp = open(fileName, 'r')
    self.n, self.e = map(int, fp.readline().split())
    self.L = [[] for _ in range(self.n)]
    for _ in range(self.e):
      i, j = map(int,fp.readline().split())
      self.L[i].append(j)
  def BFS(self, vs):
    q = Queue()
    visited = [False]*self.n
    visitOrder = []
    q.enQueue(vs)
    while not q.isEmpty():
      vx = q.deQueue()
      if not visited[vx]:
        visited[vx] = True
        visitOrder.append(vx)
        for vy in self.L[vx]:
          if not visited[vy]:
            q.enQueue(vy)
    return visitOrder
  def print(self):	
    for i in range(self.n):
      print(self.L[i])
    print()
  
def main():
  g = GraphList()
  g.readFile('graph5-12.txt')
  g.print()
  print(g.BFS(0))
  
if __name__ == '__main__':
  main()