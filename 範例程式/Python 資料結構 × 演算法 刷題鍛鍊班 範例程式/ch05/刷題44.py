class MapClass:
  def __init__(self):
    self.fourDir = [[0,1],[1,0],[0,-1],[-1,0]] #右、下、左、上
  def read(self):
    self.m, self.n = map(int, input().split())
    self.A = [[] for _ in range(self.m)]
    for i in range(self.m):
      self.A[i] = list(map(int,input().split()))
  def readFile(self,fileName):
    fp = open(fileName, 'r')
    self.m, self.n = map(int, fp.readline().split())
    self.A = [[] for _ in range(self.m)]
    for i in range(self.m):
      self.A[i] = list(map(int,fp.readline().split()))
  def print(self):	
    for i in range(self.m):
      for j in range(self.n):
        print(self.A[i][j], end = ' ')
      print()
    print()
  def MaxArea(self):
    maxCount = 0
    for i in range(self.m):
      for j in range(self.n):
        if self.A[i][j]==1:
          maxCount = max(maxCount, self.DFS(i,j))
    return maxCount
  def DFS(self, i,j):
    if not (0<=i<self.m and 0<=j<self.n and self.A[i][j]==1):
      return 0  #非陸地點
    self.A[i][j] = 2  #visited
    localCount = 0
    for x,y in self.fourDir:
      localCount += self.DFS(i+x, j+y)
    return localCount + 1  #加上自己後回傳
  
def main():
  g = MapClass()
  g.readFile('Map44.txt')
  g.print()
  print(g.MaxArea())

if __name__ == '__main__':
  main()