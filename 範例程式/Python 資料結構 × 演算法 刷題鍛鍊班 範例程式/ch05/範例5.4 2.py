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
  def DFS(self, v):
    self.visited[v] = True
    self.visitOrder.append(v)
    for u in self.L[v]:
      if not self.visited[u] :
        self.DFS(u)
  def print(self):	
    for i in range(self.n):
      print(self.L[i])
    print()
  
def main():
  g = GraphList()
  g.readFile('graph5-14.txt')
  g.print()
  g.visited = [False]*g.n
  g.visitOrder = []
  g.DFS(0)
  print(g.visitOrder)
  
if __name__ == '__main__':
  main()