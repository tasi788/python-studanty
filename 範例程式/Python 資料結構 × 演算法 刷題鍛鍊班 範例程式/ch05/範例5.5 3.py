from stackClass import *
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
  def DFS(self, vs):
    s = Stack()
    visited = [False]*self.n
    visitOrder = []
    s.push(vs)
    while not s.isEmpty():
      vx = s.pop()
      if not visited[vx]:
        visited[vx] = True
        visitOrder.append(vx)
        for vy in self.L[vx]:
          if not visited[vy]:
            s.push(vy)
    return visitOrder
  def print(self):	
    for i in range(self.n):
      print(self.L[i])
    print()
  
def main():
  g = GraphList()
  g.readFile('graph5-14.txt')
  g.print()
  print(g.DFS(0))
  
if __name__ == '__main__':
  main()