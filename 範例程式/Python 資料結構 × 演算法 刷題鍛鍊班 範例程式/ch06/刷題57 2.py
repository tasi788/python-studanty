from math import *
class BinTNode:
  def __init__( self, data=0 ) :
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
  
  def calBF(self, node):
    if not (node.left_c or node.right_c): #樹葉
      return 1
    if not self.balanced:   #已發現不平衡子樹，無須測試本子樹
      return 0
    leftH = self.calBF(node.left_c) if node.left_c else 0
    #print(f'{node.data}.leftH:{leftH}')
    rightH = self.calBF(node.right_c) if node.right_c else 0
    #print(f'{node.data}.rightH:{rightH}')
    if abs(leftH-rightH) > 1:
      self.balanced = False
      #print(f'{node.data}.balanced : {self.balanced}')
    return max(leftH, rightH)+1
  def TestAVL(self):
    self.balanced = True
    self.calBF(self.root)
t1 = BinTree()
t1.readFile('btree6-29b.txt')
t1.TestAVL()
print(t1.balanced)