from queueClass import *
class StackByQueue:
  def __init__(self):
    self.q1 = Queue()
    self.q2 = Queue()
  def isEmpty(self):
    return self.q1.isEmpty() and self.q2.isEmpty()
  def push(self, value):
    if self.q1.isEmpty():
      self.q1.enQueue(value)
      while not self.q2.isEmpty():
        self.q1.enQueue(self.q2.deQueue())
    else:
      self.q2.enQueue(value)
      while not self.q1.isEmpty():
        self.q2.enQueue(self.q1.deQueue())
  def pop(self):
    if not self.q1.isEmpty():
      return self.q1.deQueue()
    else:
      return self.q2.deQueue()
  def peek(self):
    if not self.q1.isEmpty():
      return self.q1.peekFront()
    else:
      return self.q2.peekFront()
  def print(self):
    print('from top to bottom: ', end='')
    if not self.q1.isEmpty():
      return self.q1.print()
    else:
      return self.q2.print()

s = StackByQueue()
s.push(1)
s.push(2)
s.push(3)
s.print()
print(s.pop())
print(s.peek())