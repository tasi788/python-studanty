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
  
def main():
  #g1 = WtGraph()
  g2 = WtGraph()
  #g1.read()
  g2.readFile('wtGraphList.txt')
  #g1.print()
  g2.print()
  
if __name__ == '__main__':
  main()