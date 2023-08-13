class BinTNode:
  def __init__( self, data=0 ) :		# data的預設值為0
    self.data = data
    self.left_c = None
    self.right_c = None
class BinTree:
  def __init__(self):
    self.root = None
  def read(self):
    self.nodes = list(input().split())
    self.current = 0
    self.root = self.create()
  def create(self):
    nodedata = self.nodes[self.current]
    self.current += 1
    if nodedata == '0': return
    node = BinTNode(nodedata)
    node.left_c = self.create()
    node.right_c = self.create()
    return node
  def countNode(self, p):
    if not p: return
    self.n += 1
    self.countNode(p.left_c)
    self.countNode(p.right_c)
  def readFile(self,fileName):
    fp = open(fileName, 'r')
    self.nodes = list(fp.readline().split())
    self.current = 0
    self.root = self.create()  
  def preorder(self, p):
    if not p: return
    print(p.data, end = ' ')
    self.preorder(p.left_c)
    self.preorder(p.right_c)
  
def main():
  t = BinTree()
  t.readFile('btree6-7b.txt')
  #t.preorder(t.root)
  t.n = 0
  t.countNode(t.root)
  print(t.n)
  
main()