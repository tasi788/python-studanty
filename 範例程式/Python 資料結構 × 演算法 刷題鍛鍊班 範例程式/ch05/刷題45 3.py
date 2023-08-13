class WtGraph:
  def read(self):
    self.n, self.e = map(int, input().split())
    self.L = [[] for _ in range(self.n)]
    for _ in range(self.e):
      i, j, w = map(int,input().split())
      self.L[i].append((j,w))
  def readFile(self,fileName):
    fp = open(fileName, 'r')
    self.n, self.e = map(int, fp.readline().split())
    self.L = [[] for _ in range(self.n)]
    for _ in range(self.e):
      i, j, w = map(int,fp.readline().split())
      self.L[i].append((j,w))
  def print(self):	
    for i in range(self.n):
      print(self.L[i])
    print()
  def MCST(self):
    self.T = []
    self.candidate = []
    self.fillCandi()
    sum = 0
    while len(self.T)<self.n-1:
      edge = self.candidate.pop(0)
      if not self.testCycle(edge):
        self.T.append(edge)
        sum += edge[0]
    return sum
  def fillCandi(self):
    for u in range(len(self.L)):
      for e in self.L[u]:
        v, w = e[0], e[1]
        if (w,v,u) not in self.candidate:
          self.candidate.append((w,u,v))
    self.candidate.sort()
        
  def testCycle(self,addedge):
    findu = findv = False
    for e in self.T:
      if e[1]==addedge[1] or e[1]==addedge[2]:
        findu = True
      if e[2]==addedge[1] or e[2]==addedge[2]:
        findv = True
    return findu and findv
      
def main():
  g2 = WtGraph()
  g2.readFile('wtGraphList.txt')
  g2.print()
  print(g2.MCST())
  
if __name__ == '__main__':
  main()
