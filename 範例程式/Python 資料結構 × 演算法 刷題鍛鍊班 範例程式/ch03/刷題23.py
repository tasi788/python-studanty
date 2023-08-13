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
  def reverse(self):
    if self._size < 2: 	#節點數0或1個，無須動作
      return
    p = self._head
    q = p.next
    r = q.next
    p.next = None
    while q is not None:
      q.next = p		#反轉第二個節點的指標
      p = q			# p, q, r都各往右一步
      q = r
      if r: r = r.next
    self._head = p	#原本最後節點變成第一個節點
  
def main():
  a = LinkedList()
  a.append(10)
  a.append(20)
  a.append(30)
  a.append(40)
  a.print()
  a.reverse()
  a.print()
  
if __name__ == '__main__':
  main()