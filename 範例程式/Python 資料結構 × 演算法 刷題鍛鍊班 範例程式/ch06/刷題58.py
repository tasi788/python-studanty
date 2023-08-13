from queue import PriorityQueue
class BinTNode:
  def __init__(self, data):
    self.data = data
    self.left_c = None
    self.right_c = None

class StickConnection:
  def __init__(self):
    self.ws = list(map(int, input().split())) #weights
    self.totalLen = 0
    pq = PriorityQueue()
    for i in range(len(self.ws)):
      pq.put((self.ws[i], BinTNode(self.ws[i])))
    while pq.qsize() > 1:
      w1, node1 = pq.get()
      w2, node2 = pq.get()
      newnode = BinTNode(w1+w2)
      newnode.left_c = node1
      newnode.right_c = node2
      pq.put((w1+w2, newnode))
      self.totalLen += (w1+w2)
      
w = StickConnection()
print(w.totalLen)
#輸入範例
#2 9 5
#輸出 23