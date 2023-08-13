from LinkedListClass import *	#LinkedListClass.py 有類別定義
def MergeTwoList(a, b):
  p = a._head			# p 從串列a的第一個節點開始
  q = b._head			# q 從串列b的第一個節點開始
  c = LinkedList()				# 新增空串列c
  while p and q:				# 兩個串列都未用完
    if p.data < q.data:
      c.append(p.data)		# 串列a貢獻資料
      p = p.next				# p往右一個節點
    elif p.data > q.data:		# 串列b貢獻資料
      c.append(q.data)		# q往右一個節點
      q = q.next
    else:					# a, b都貢獻資料 
      c.append(p.data)		
      p = p.next
      c.append(q.data)		
      q = q.next
  while p:					# 串列a尚未用完
    c.append(p.data)
    p = p.next
  while q:					# 串列b尚未用完
    c.append(q.data)
    q = q.next
  return c

a = LinkedList()
a.append(2)
a.append(2)
#a.append(8)
b = LinkedList()
b.append(2)
b.append(3)
b.append(5)      
c = MergeTwoList(a, b)
c.print()	