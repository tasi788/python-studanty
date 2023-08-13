class  PListNode:
  def __init__(self, coef=1, expo=0):
    self.coef = coef
    self.expo = expo
    self.next = None

class PLinkedList:
  def __init__(self):
    self._head = None
    self._size = 0
  def len(self):
    return self._size
  def insert(self, p, co, ex):
    new_node = PListNode(co, ex)
    if self._head is None:
      self._head = new_node
    else:
      new_node.next = p.next
      p.next = new_node
    return new_node
  def print(self):
    p = self._head
    while p.next:
      print(f'{p.coef}x^{p.expo} + ', end = '')
      p = p.next
    print(f'{p.coef}x^{p.expo}')
  
def PolyAdd(a, b):
  c = PLinkedList()
  ctail = None
  pa = a._head
  pb = b._head
  while pa is not None and pb is not None:	
    if pa.expo > pb.expo:
      ctail = c.insert(ctail, pa.coef, pa.expo)
      pa = pa.next
    elif pa.expo < pb.expo:	
      ctail = c.insert(ctail, pb.coef, pb.expo)
      pb = pb.next
    else:
      if pa.coef + pb.coef != 0:	
        ctail = c.insert(ctail, pa.coef+pb.coef, pa.expo)
        pa = pa.next
        pb = pb.next
  while pa is not None:	
    ctail = c.insert(ctail, pa.coef, pa.expo)
    pa = pa.next
  while pb is not None: 
    ctail = c.insert(ctail, pb.coef, pb.expo)
    pb = pb.next
  return c

a = PLinkedList()
tail = None
tail = a.insert(tail,5,4)
tail = a.insert(tail, 6.1,2)
tail = a.insert(tail, 2.9,1)
tail = a.insert(tail, 6,0)
a.print()

b = PLinkedList()
tail = None
tail = b.insert(tail,9,5)
tail = b.insert(tail, 3.2,2)
tail = b.insert(tail, 4,1)
tail = b.insert(tail, 5,0)
b.print()

c = PolyAdd(a,b)
c.print()