class Tree:
  def read(self):
    self.n = int(input())
    self.L = [[] for _ in range(self.n)]
    for _ in range(self.n - 1):
      i, j = map(int,input().split())
      self.L[i].append(j)
  def readFile(self,fileName):
    fp = open(fileName, 'r')
    self.n = int(fp.readline())
    self.L = [[] for _ in range(self.n)]
    for _ in range(self.n-1):
      i, j = map(int,fp.readline().split())
      self.L[i].append(j)
  def findRoot(self):
    indegree = [0] * self.n
    for u in range(self.n):
      for v in self.L[u]:
        indegree[v] += 1
    return indegree.index(0)
  def findDis(self, u):
    if len(self.L[u]) == 0:
      return 1
    first = second = 0
    for v in self.L[u]:
      h = self.findDis(v)
      if h > first:
        second = first
        first = h
      elif h > second:
        second = h
    self.maxDis = max(self.maxDis, first+second)
    return first+1
      
def main():
  t = Tree()
  t.readFile('tree6-1.txt')
  t.maxDis = 0
  t.findDis(t.findRoot())
  print(t.maxDis)
    
if __name__ == '__main__':
  main()