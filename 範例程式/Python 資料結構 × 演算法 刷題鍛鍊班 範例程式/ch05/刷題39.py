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
  def print(self):	
    for i in range(self.n):
      print(self.L[i])
    print()
  def hasPath(self, v, target):
    if self.colorV[v] == self.WHITE:
      self.colorV[v] = self.GREY
      if v == target:
        self.findFlag = True
        return
      for j in self.L[v]:
        if self.findFlag == True:
          return
        if self.colorV[j] == self.WHITE:
          self.hasPath(j, target)
      self.colorV[v] = self.BLACK
  
def main():
  g = Graph()
  g.readFile('graph5-15.txt')
  g.print()
  start, target = map(int, input().split())
  g.colorV = [g.WHITE]*g.n
  g.findFlag = False
  g.hasPath(start,target)
  print(g.findFlag)
  
if __name__ == '__main__':
  main()