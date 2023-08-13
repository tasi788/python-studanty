from LinkedListClass import *

def sumTwoList(a, b):
  p = a._head			# p 從串列a的第一個節點開始
  q = b._head			# q 從串列b的第一個節點開始
  carry = 0
  c = LinkedList()				# 新增空串列c
  while p and q:				# 兩個串列都未用完
    result = p.data + q.data + carry
    c.append(result % 10)		# 本位數相加結果
    carry = result // 10		#進位值
    p = p.next 
    q = q.next
  while p:					# 串列a尚未用完
    result = p.data + carry
    c.append(result % 10)
    carry = result // 10
    p = p.next
  while q:					# 串列b尚未用完
    result = q.data + carry
    c.append(result % 10)
    carry = result // 10
    q = q.next
  if carry:
    c.append(carry)
  return c

a = LinkedList()
a.append(9)
a.append(2)
a.append(8)
b = LinkedList()
b.append(4)
b.append(5)
b.append(3)
c = sumTwoList(a,b)
c.print()
