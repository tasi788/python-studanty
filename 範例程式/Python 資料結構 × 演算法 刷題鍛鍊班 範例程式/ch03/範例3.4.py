class ListNode:
  def __init__(self, data=0):
    self.data = data
    self.next = None
def  append(head, value):
  p = head
  new_node = ListNode(value)	#產生新節點
  while p.next != None:		#迴圈結束後p會指向最後一個節點
    p = p.next
  p.next = new_node			#改變原來最後節點的指標
def traversal( head ):
  p = head
  while p is not None :
    print(p.data, end = ' ')
    p = p.next
  print()
def  delete(head, value):  		#從串列中刪除data為value的節點
  old_node = head				#從第一個節點開始
  pre_node = None				#pre_node緊跟在old_node左邊
  while old_node != None:			#串列尚未比完
    if old_node.data == value:		#找到要刪除的節點則離開迴圈
      break
    pre_node = old_node			#移到次一節點繼續搜尋
    old_node = old_node.next
  if old_node != None:				#有找到要刪除的節點
    if pre_node == None:			#要刪除的是第一個節點
      new_head = old_node.next	#原來第二個節點成為新的第一節點
      del old_node
      return new_head			#傳回新的第一節點
    pre_node.next = old_node.next	#正常刪除
    del old_node 
  return head

a = ListNode(20)
append(a, 50)
append(a, 70)
append(a, 90)
traversal(a)
a = delete(a, 70)
traversal(a)