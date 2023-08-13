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
  def  find(self, value):#尋找值為value的節點並回傳
    p = self._head					#從第一個節點開始
    while p != None:			#串列尚未比完
      if p.data == value:			#搜尋成功
        return p
      p = p.next				#不相等，移到次一節點
    return None				# p已經走完，搜尋失敗
  def insertAfter(self, p, value):
    new_node = ListNode(value)	#產生新節點
    self._size += 1
    if p == None:#加在最前
      new_node.next = self._head
      self._head = new_node
      return
    new_node.next = p.next
    p.next = new_node
  def  delete(self, value):  	#從串列中刪除data為value的節點
    old_node = self._head				#從第一個節點開始
    pre_node = None				#pre_node緊跟在old_node左邊
    while old_node != None:			#串列尚未比完
      if old_node.data == value:	#找到要刪除的節點則離開迴圈
        break
      pre_node = old_node			#移到次一節點繼續搜尋
      old_node = old_node.next
    if old_node != None:				#有找到要刪除的節點
      if pre_node == None:			#要刪除的是第一個節點
        self._head = old_node.next	#原來第二個節點成為新的第一節點
      else:
        pre_node.next = old_node.next	#正常刪除
      del old_node 

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
  def reverse2(self, p, q, r):
    if r is None:
      q.next = p
      self._head = q
    else:
      self.reverse2(q, r, r.next)
      q.next = p
def main():
  a = LinkedList()
  a.insertAfter(None, 99)
  a.append(4)
  a.append(1)
  p = a.find(4)
  a.insertAfter(p, 444)
  a.append(8)
  a.append(5)
  a.append(4)
  #a.reverse()
  a.print()
  a.delete(99)
  a.print()

if __name__ == '__main__':
  main()