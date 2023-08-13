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
def  find(head, value):  		#尋找值為value的節點並回傳
  p = head					#從第一個節點開始
  while p != None:			#串列尚未比完
    if p.data == value:			#搜尋成功
      return p
    p = p.next				#不相等，移到次一節點
  return None

a = ListNode(20)
append(a, 50)
append(a, 70)
p = find(a, 50)
if p: print(p.data)
p = find(a, 90)
if not p: print("find failed!")