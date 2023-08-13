class Graph:
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
      for j in self.L[v]:
        if self.colorV[j] == self.WHITE:
          self.DFS(j)
      self.colorV[v] = self.BLACK
  def print(self):	
    for i in range(self.n):
      print(self.L[i])
    print()
  def isConnected(self):
    self.DFS(0)
    if self.colorV.count(self.WHITE):#有未訪頂點
      return False
    return True

g1 = Graph()
g1.readFile('graph5-16.txt') #若讀入graph-5-16-1.txt則回報True
g1.print()
g1.colorV = [g1.WHITE]*g1.n
print(g1.isConnected())