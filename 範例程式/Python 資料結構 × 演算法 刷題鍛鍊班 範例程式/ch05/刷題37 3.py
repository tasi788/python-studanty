from queueClass import *
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
  def BFS_test(self, vs, vd):
    q = Queue()
    visited = [False]*self.n
    q.enQueue(vs)
    while not q.isEmpty():
      vx = q.deQueue()
      if vx == vd:
        return True
      if not visited[vx]:
        visited[vx] = True
        for vy in self.L[vx]:
          if not visited[vy]:
            q.enQueue(vy)
    return False  
  def print(self):	
    for i in range(self.n):
      print(self.L[i])
    print()
  
def main():
  g = GraphList()
  g.readFile('graph#37.txt')
  g.print()
  src, dst = map(int, input().split())
  print(g.BFS_test(src, dst))
  
if __name__ == '__main__':
  main()