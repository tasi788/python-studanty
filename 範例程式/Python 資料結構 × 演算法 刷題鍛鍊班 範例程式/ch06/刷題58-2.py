from queue import PriorityQueue
class StickConnection:
  def __init__(self):
    self.ws = list(map(int, input().split())) #weights
    self.totalLen = 0
    pq = PriorityQueue()
    for i in range(len(self.ws)):
      pq.put(self.ws[i])
    while pq.qsize() > 1:
      w1 = pq.get()
      w2 = pq.get()
      pq.put(w1+w2)
      self.totalLen += (w1+w2)
      
w = StickConnection()
print(w.totalLen)
#輸入範例
#2 9 5
#輸出 23