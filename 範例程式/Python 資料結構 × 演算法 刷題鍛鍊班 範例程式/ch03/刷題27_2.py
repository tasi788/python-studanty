from LinkedListClass import *	#LinkedListClass.py 有類別定義
def intersection2(a, b):
  if a.len() < b.len():			#串列a設為長串列
    a, b = b, a
  p = a._head				# p 跳過前段
  for _ in range(a.len() - b.len()):
    p = p.next
  q = b._head				# q 從串列b的第一個節點開始
  fromHere = None
  while p and q:				# 兩個串列都未用完
    if p.data == q.data:
      if fromHere is None:
        fromHere = p.data	# 紀錄最新交集起始
    else:
      fromHere = None		# 清除紀錄
    p = p.next				# p, q往右一個節點
    q = q.next
  return fromHere

a = LinkedList()
a.append(9)
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
print(intersection2(a, b))