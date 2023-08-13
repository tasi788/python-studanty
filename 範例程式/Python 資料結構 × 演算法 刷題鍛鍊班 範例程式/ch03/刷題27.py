from LinkedListClass import *	#LinkedListClass.py 有類別定義
def intersection(a, b):
  a.reverse()					#反轉串列a
  p = a._head				# p 從串列a的第一個節點開始
  b.reverse()					#反轉串列b
  q = b._head				# q 從串列b的第一個節點開始
  result = None
  while p and q:				# 兩個串列都未用完
    if p.data == q.data:
      result = p.data			# 紀錄最新交集
      p = p.next				# p, q往右一個節點
      q = q.next
    else:					# 交集結束 
      return result
  return result

a = LinkedList()
a.append(4)
a.append(1)
a.append(8)
a.append(5)
a.append(4)
b = LinkedList()
b.append(5)
b.append(6)
b.append(1) 
b.append(8)
b.append(5)
b.append(4)     
print(intersection(a, b))