class BinTNode:
  def __init__( self, data) :		
    self.data = data
    self.left_c = None
    self.right_c = None
class BST:
  def __init__(self):
    self.root = None
  def create(self):
    self.nodes = list(input().split())
    for nodedata in self.nodes:
      node = BinTNode(nodedata)
      self.insert(node)
  def insert(self, newnode):
    LEFT, RIGHT = range(2)
    if not self.root:  #空樹
      self.root = newnode
      return
    current = self.root
    while current:
      curParent = current
      if newnode.data < current.data:
        direction = LEFT
        current = current.left_c
      elif newnode.data > current.data:
        direction = RIGHT
        current = current.right_c
      else:
        return  #資料已在樹上
    if direction == LEFT:
      curParent.left_c = newnode
    else:
      curParent.right_c = newnode
  def createFromFile(self,fileName):
    fp = open(fileName, 'r')
    self.nodes = list(fp.readline().split())
    for nodedata in self.nodes:
      node = BinTNode(nodedata)
      self.insert(node)
  def preorder(self, p):
    if not p: return
    print(p.data, end = ' ')
    self.preorder(p.left_c)
    self.preorder(p.right_c)
  def search(self, key):
    current = self.root
    while current:
      if key < current.data:
        current = current.left_c
      elif key > current.data:
        current = current.right_c
      else:
        return  True #資料在樹上
    return False
def main():
  t = BST()
  t.createFromFile('bst6-28.txt')  #或 t.create()
  t.preorder(t.root)
  print()
  key = input()
  print(t.search(key))
      
if __name__ == '__main__':
  main()