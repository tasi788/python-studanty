class Queue:
  def __init__(self):
    self.item = list()
  #檢查堆疊是否已空的method
  def isEmpty(self):
    return len(self.item) == 0
  #檢查堆疊是否已滿的method
  def isFull(self):
    return False
  # 推入新資料的method
  def enQueue(self, value):
    self.item.append(value)	
  # 彈出資料的method
  def deQueue(self):
    if not self.isEmpty():
      return self.item.pop(0)
    return None
  def peekFront(self):
    if not self.isEmpty():
      return self.item[0]
    return None
  def peekRear(self):
    if not self.isEmpty():
      return self.item[-1]
    return None
  #印出資料的method
  def print(self):		#bottom up
    for i in range(len(self.item)):
      print(self.item[i], end = ' ')
    print()
  
def main():
  a = Queue()
  print(a.isEmpty())
  a.enQueue(4)
  a.enQueue(5)
  a.enQueue(6)
  print(a.deQueue())
  a.print()

if __name__ == '__main__':
  main()