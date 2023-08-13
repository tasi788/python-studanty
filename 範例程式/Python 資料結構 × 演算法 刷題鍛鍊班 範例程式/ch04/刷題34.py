from stackClass import *
class QueueByStack:
  def __init__(self):
    self.s1 = Stack()
    self.s2 = Stack()
  def isEmpty(self):
    return self.s1.isEmpty()
  def enQueue(self, value):
    while not self.s1.isEmpty():
      self.s2.push(self.s1.pop())
    self.s1.push(value)
    while not self.s2.isEmpty():
      self.s1.push(self.s2.pop())
  def deQueue(self):
    if not self.s1.isEmpty():
      return self.s1.pop()
  def peekFront(self):
    if not self.s1.isEmpty():
      return self.s1.peek()
  def peekRear(self):
    if not self.s1.isEmpty():
      return self.s1.item[0]
  def print(self):
    if not self.s1.isEmpty():
      return self.s1.print()
    else:
      return self.s2.print()

q = QueueByStack()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
print(q.isEmpty())
q.enQueue(4)
q.print()
print(q.deQueue())
print(q.peekFront())
print(q.peekRear())