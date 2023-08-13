class BinTNode:
  def __init__( self, data=0 ) :		# data的預設值為0
    self.data = data
    self.left_c = None
    self.right_c = None
class BinTree:
  def __init__(self):
    self.root = None
  def createByInPre(self):
    self.inorder = list(input().split())
    self.preorder = list(input().split())
    n = len(self.inorder)
    self.root = self.create(0, n-1, 0, n-1)
  def create(self, inLeft, inRight, preLeft, preRight):
    if inLeft > inRight or preLeft > preRight: 
      return None
    d = self.preorder[preLeft]
    m = self.inorder.index(d)
    m1 = m - inLeft
    node = BinTNode(d)
    node.left_c = self.create(inLeft, m-1, preLeft+1, preLeft+m1)
    node.right_c = self.create(m+1,inRight,preLeft+m1+1,preRight )
    return node
  
  def postorder(self, p):
    if not p: return
    self.postorder(p.left_c)
    self.postorder(p.right_c)
    print(p.data, end = ' ')
def main():
  t = BinTree()
  t.createByInPre()
  t.postorder(t.root)
    
if __name__ == '__main__':
  main()
#輸入範例
# D F B A C G E H
# A B D F C E G H
#輸出 F D B G H E C A