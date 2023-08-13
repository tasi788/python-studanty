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
    if not self.visited[vs]:
      self.visited[vs] = True
      print(vs, end = ' ')
      for j in self.L[vs]:
        if not self.visited[j]:
          self.DFS(j)
  def print(self):	
    for i in range(self.n):
      print(self.L[i])
    print()
  
def main():
  g = GraphList()
  g.readFile('graphList.txt')
  g.print()
  
if __name__ == '__main__':
  main()