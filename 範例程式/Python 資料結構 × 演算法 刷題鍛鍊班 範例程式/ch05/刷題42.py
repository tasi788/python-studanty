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
  def DFS2(self, vs):
    if self.colorV[vs] == self.WHITE:  #vs未被走訪
      self.colorV[vs] = self.GREY      #走訪中
      for j in self.L[vs]:
        if self.findFlag: return
        if self.colorV[j] == self.GREY :#j走訪中
          self.findFlag = True            #發現死結
        else:
          self.DFS2(j)
      self.colorV[vs]= self.BLACK      # vs完成走訪，回溯上一層
  def print(self):	
    for i in range(self.n):
      print(self.L[i])
    print()
  def hasCycle(self):
    self.colorV = [self.WHITE] * self.n
    self.findFlag = False
    unvisitV = self.colorV.count(self.WHITE) #未訪頂點數
    while unvisitV and not self.findFlag:
      v = self.colorV.index(self.WHITE)
      self.DFS2(v)
      unvisitV = self.colorV.count(self.WHITE)
    return self.findFlag

g1 = GraphList()
g1.readFile("graph5-17.txt")
g1.print()
print(not g1.hasCycle())