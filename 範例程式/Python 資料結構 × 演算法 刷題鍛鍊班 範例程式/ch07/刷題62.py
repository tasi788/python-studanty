class ListNode:
  def __init__( self, data=0 ) :		
    self.data = data
    self.next = None
class LinkedList:
  def __init__(self):
    self._head = None	
    self._size = 0
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
  def sort(self):
    left = self._head    #每回合最左節點
    while left:          #本回合範圍內尚有節點須排序
      min_pos = left     #初設最左節點為目前最小
      p = left.next      #第二個節點先當挑戰者
      while p:               #尚有挑戰者
        if p.data < min_pos.data:
          min_pos = p        #挑戰成功，霸主換人
        p = p.next          #下一個挑戰者
      min_pos.data, left.data = left.data, min_pos.data
      left = left.next  #下一回合左限右移一個節點
  
def main():
  a = LinkedList()
  a.append(4)
  a.append(1)
  a.append(8)
  a.append(5)
  a.print()
  a.sort()
  a.print()

if __name__ == '__main__':
  main()