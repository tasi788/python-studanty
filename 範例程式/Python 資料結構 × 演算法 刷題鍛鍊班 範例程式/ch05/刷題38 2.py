class GraphList:
  WHITE, GREY, BLACK = range(3)
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
    if self.colorV[v] == self.WHITE:
      self.colorV[v] = self.GREY
      self.visitOrder.append(v)
      for j in self.L[v]:
        if self.colorV[j] == self.WHITE:
          self.DFS(j)
      self.colorV[v] = self.BLACK
  def print(self):	
    for i in range(self.n):
      print(self.L[i])
    print()
  
def main():
  g = GraphList()
  g.readFile('graph5-14.txt')
  g.print()
  g.colorV = [g.WHITE]*g.n
  g.visitOrder = []
  g.DFS(0)
  print(g.visitOrder)
  
if __name__ == '__main__':
  main()