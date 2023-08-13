class ListNode:
  def __init__(self, data=0):
    self.data = data
    self.next = None

def traversal( head ):
  p = head
  while p is not None :
    print(p.data, end = ' ')
    p = p.next
  print()
def  append(head, value):
  p = head
  new_node = ListNode(value)	#產生新節點
  while p.next != None:		#迴圈結束後p會指向最後一個節點
    p = p.next
  p.next = new_node			#改變原來最後節點的指標
  
a = ListNode(20)
append(a, 50)
append(a, 70)
append(a, 90)
traversal(a)