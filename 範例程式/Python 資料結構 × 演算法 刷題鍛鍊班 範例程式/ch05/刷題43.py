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
    for e in range(self.e):
      i, j = map(int,fp.readline().split())
      self.L[i].append(j)
  def DFS2(self, v):
    if self.colorV[v] == self.WHITE:
      self.colorV[v] = self.GREY
      for j in self.L[v]:
        if self.findFlag: return
        if (j,v) not in self.visitE:
          if self.colorV[j] == self.GREY :#j走訪中
            self.findFlag = True
          else:
            self.visitE.append((v,j))
            self.DFS2(j)
      self.colorV[v] = self.BLACK    
  def print(self):	
    for i in range(self.n):
      print(self.L[i])
    print()
  def hasCycle(self):
    self.colorV = [self.WHITE] * self.n
    self.findFlag = False
    self.visitE = []
    unvisitV = self.colorV.count(self.WHITE) #未訪頂點數
    while unvisitV and not self.findFlag:
      v = self.colorV.index(self.WHITE)
      self.DFS2(v)
      unvisitV = self.colorV.count(self.WHITE)
    return self.findFlag

g1 = GraphList()
g1.readFile('graph5-18.txt')
g1.print()
print(g1.hasCycle())
