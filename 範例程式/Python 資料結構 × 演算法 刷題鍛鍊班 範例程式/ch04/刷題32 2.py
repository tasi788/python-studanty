class CircularQueue:
  MAX_ITEM = 7						#預設的最大空間
  def __init__(self, maxsize=MAX_ITEM):
    self.maxsize = maxsize
    self.item = [0]*maxsize
    self.front = 1
    self.rear = self.size = 0
  def isEmpty(self): 					#檢查佇列是否已空的method
    return self.size == 0
  def isFull(self): 					#檢查佇列是否已滿的method
    return self.size == self.maxsize
  def enQueue(self, value):			# 加入新資料的method
    if self.isFull(): return False #佇列已滿，加入
    self.rear = (self.rear+1) % self.maxsize  #rear順時針推進1格
    self.item[self.rear] = value
    self.size += 1
    return True
  def deQueue(self): 					#取出資料的method
    if self.isEmpty(): return None  #佇列為空，無取出
    data = self.item[self.front]
    self.size -= 1
    self.front = (self.front+1) % self.maxsize 
    return data
  def peekRear(self):
    if self.isEmpty(): return None
    return self.item[self.rear]
  def peekFront(self):
    if self.isEmpty(): return None
    return self.item[self.front]
    
a = CircularQueue(3)
print(a.enQueue(33))
print(a.enQueue(44))
print(a.deQueue())
print(a.enQueue(55))
print(a.enQueue(66))
print(a.enQueue(77))
print(a.isFull())
print(a.peekFront())
print(a.peekRear())