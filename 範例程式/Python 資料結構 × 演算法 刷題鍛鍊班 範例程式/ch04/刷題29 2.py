class MinStack:
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
    minvalue = min(value, self.getMin())
    self.item.append((value, minvalue))
  # 取得堆疊最小值的method
  def getMin(self):
    if len(self.item) == 0:
      return float('inf')
    return self.item[-1][1]	
  # 彈出資料的method
  def pop(self):
    if not self.isEmpty():
      value, minvalue = self.item.pop()
      return value
    return None
  #查看頂端資料的method
  def peek(self):
    if not self.isEmpty():
      return self.item[-1][0]
    return None
  #印出資料的method
  def print(self):		#from top to bottom
    print('from top to bottom: ', end='')
    for i in range(1, len(self.item)+1):
      print(self.item[-i][0], end = ' ')
    print()
  
def main():
  a = MinStack()
  a.push(6)
  a.push(4)
  a.push(8)
  print(a.getMin())
  print(a.pop())
  a.push(9)
  print(a.getMin())
  a.print()

if __name__ == '__main__':
  main()