from queue import PriorityQueue
class BinTNode:
  def __init__(self, data):
    self.data = data
    self.left_c = None
    self.right_c = None

class HuffmanCode:
  def __init__(self):
    self.chs = list(input().split()) #characters
    self.fs = list(map(float, input().split())) #frequencies
    self.codes = [None]*len(self.chs)  #encoding results of each ch
    pq = PriorityQueue()
    for i in range(len(self.chs)):
      pq.put((self.fs[i], self.chs[i], BinTNode(self.chs[i])))
    while pq.qsize() > 1:
      f1, a1, node1 = pq.get()
      f2, a2, node2 = pq.get()
      newnode = BinTNode("X")
      newnode.left_c = node1
      newnode.right_c = node2
      pq.put((f1+f2, "X", newnode))
      
    f,a, root = pq.get()
    #self.preorder(root)
    self.curcode = []
    self.encodeTable(root)
    for i in range(len(self.chs)):
      print(self.chs[i], self.codes[i])
  def preorder(self, node):
    if not node: return
    print(node.data)
    self.preorder(node.left_c)
    self.preorder(node.right_c)
    
  def encodeTable(self, node):
    if not (node.left_c or node.right_c): #leaf
      i = self.chs.index(node.data)
      self.codes[i] = "".join(self.curcode)
      self.curcode.pop()
      return
    self.curcode.append("0")
    self.encodeTable(node.left_c)
    self.curcode.append("1")
    self.encodeTable(node.right_c)
    if len(self.curcode):
      self.curcode.pop()
    
HuffmanCode()
#輸入範例
#A B C D E F
#15 8 30 27 5 15
#輸出
#A 101
#B 1001
#C 11
#D 01
#E 1000
#F 00