class GraphMatrix:
  def read(self):
    self.n = int(input())
    self.A = [[] for _ in range(self.n)]
    for i in range(self.n):
      self.A[i] = list(map(int,input().split()))
  def readFile(self,fileName):
    fp = open(fileName, 'r')
    self.n = int(fp.readline())
    self.A = [[] for _ in range(self.n)]
    for i in range(self.n):
      self.A[i] = list(map(int,fp.readline().split()))
  def print(self):	
    for i in range(self.n):
      for j in range(self.n):
        print(self.A[i][j], end = ' ')
      print()
    print()
  
def main():
  g = GraphMatrix()
  #g.read()
  g.readFile('graphArray.txt')
  g.print()

if __name__ == '__main__':
  main()