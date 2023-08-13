class Stack:
  def __init__(self):
    self.item = list()
  #檢查堆疊是否已空的method
  def isEmpty(self):
    return len(self.item) == 0
  #檢查堆疊是否已滿的method
  def isFull(self):
    return False
  # 推入新資料的method
  def push(self, value):
    self.item.append(value)	
  # 彈出資料的method
  def pop(self):
    if not self.isEmpty():
      return self.item.pop()
    return None
  #查看頂端資料的method
  def peek(self):
    if not self.isEmpty():
      return self.item[-1]
    return None
  #印出資料的method
  def print(self):		#up botton
    print("top to bottom: ", end='')
    for i in range(1, len(self.item)+1):
      print(self.item[-i], end = ' ')
    print()
  
def main():
  a = Stack()
  print(a.isEmpty())
  a.push(4)
  a.push(5)
  print(a.pop())
  a.push(6)
  print(a.peek())
  a.print()

if __name__ == '__main__':
  main()