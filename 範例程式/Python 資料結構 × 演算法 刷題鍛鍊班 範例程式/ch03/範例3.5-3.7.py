class DListNode:
  def __init__( self, data=0 ) :		# data的預設值為0
    self.data = data
    self.left = self.right = None
	  
class DLinkedList:
  def __init__(self):
    self._head = None			#初始時沒有節點
    self._size = 0
	# 回傳節點個數
  def len(self):
    return self._size
  # 插入新節點
  def insert(self, p, value):
    new_node = DListNode(value)
    new_node.left = p
    new_node.right = p.right
    p.right.left = new_node
    p.right = new_node
  # 附加新節點
  def append(self, value):
    p = self._head
    new_node = DListNode(value)	#產生新節點
    self._size += 1
    if p == None:
      self._head = new_node
    else:
      while p.right != None:		
        p = p.right
      p.right = new_node
      new_node.left = p		
  # 搜尋節點
  def find(self, value):
    p = self._head
    while p:
      if p.data == value:
        return p
      p = p.right
      if p == self._head:
        break
    return None
  # 刪除節點
  def delete(self, p):
    p.left.right = p.right
    p.right.left = p.left
    del p
    self._size -= 1
    if self._size == 0:
      self._head = None
  #印出串列
  def print(self):
    p = self._head
    while p is not None :
      print(p.data, end = ' ')
      p = p.right
    print()

def main():
  a = DLinkedList()
  a.append(10)
  a.append(20)
  a.append(40)
  a.print()
  p = a.find(20)
  a.insert(p, 35)
  a.print()
  p = a.find(35)
  a.delete(p)
  a.print()
  
if __name__ == '__main__':
  main()