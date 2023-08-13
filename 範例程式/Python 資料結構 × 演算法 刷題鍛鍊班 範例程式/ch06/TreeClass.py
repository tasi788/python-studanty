from queueClass import *
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
  def print(self):	
    for i in range(self.n):
      print(self.L[i])
    print()
  
def main():
  t = Tree()
  t.readFile('tree6-1.txt')
  t.print()
    
if __name__ == '__main__':
  main()