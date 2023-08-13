class maxHeap:
  def __init__(self):
    self.nodes = []
  def put(self, data):
    self.nodes.append(data)
    i = len(self.nodes) - 1
    while i > 0:
      f = (i-1)//2
      if self.nodes[f]<self.nodes[i]:
        self.nodes[f],self.nodes[i]=self.nodes[i],self.nodes[f]
        i = f
      else:
        break
  def get(self):
    if len(self.nodes) == 0:
      return None
    root = self.nodes[0]
    up = self.nodes[len(self.nodes)-1]
    del(self.nodes[-1])
    k = 0
    while k < len(self.nodes)//2:
      bc = 2*k + 1
      if bc+1<len(self.nodes) and self.nodes[bc+1]>self.nodes[bc]:
        bc += 1
      if up >= self.nodes[bc]:
        break
      self.nodes[k] = self.nodes[bc]
      k = bc
    self.nodes[k] = up
    return root

nums = list(map(int, input().split()))
maxh = maxHeap()
for num in nums:
  maxh.put(num)
  print(maxh.nodes)
print(maxh.get())
print(maxh.nodes)
print(maxh.get())
print(maxh.nodes)