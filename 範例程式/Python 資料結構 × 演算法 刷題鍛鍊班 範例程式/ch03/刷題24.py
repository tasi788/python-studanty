class ListNode:
  def __init__( self, data=0 ) :		
    self.data = data
    self.next = None
class LinkedList:
  def __init__(self):
    self._head = None	
    self._size = 0
  def len(self):
    return self._size
  def append(self, value):
    p = self._head
    new_node = ListNode(value)	#產生新節點
    self._size += 1
    if p == None:
      self._head = new_node
      return
    while p.next != None:		
      p = p.next
    p.next = new_node
  def print(self):		#之前命名為traversal
    p = self._head
    while p is not None :
      print(p.data, end = ' ')
      p = p.next
    print()
  def reverse2(self, p, q, r):
    if r is None:
      q.next = p
      self._head = q
    else:
      self.reverse2(q, r, r.next)
      q.next = p
  
def main():
  a = LinkedList()
  a.append(10)
  a.append(20)
  a.append(30)
  a.append(40)
  a.print()
  a.reverse2(None, a._head, a._head.next)
  a.print()
  
if __name__ == '__main__':
  main()