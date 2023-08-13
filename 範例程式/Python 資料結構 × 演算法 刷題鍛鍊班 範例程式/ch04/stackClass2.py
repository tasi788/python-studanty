#stack with limited space
MAXSIZE = 10000
class Stack:
  def __init__(self, maxsize = MAXSIZE):
    self._maxsize = maxsize
    self._item = [0]*maxsize
    self._top = -1			#初始時沒有資料
  #檢查堆疊是否已空
  def isEmpty(self):
    if self._top < 0:
      return True
    return False
  #檢查堆疊是否已滿
  def isFull(self):
    if self._top >= self._maxsize-1 :
      return True
    return False
  # 推入新資料
  def push(self, value):
    if not self.isFull():
      self._top += 1
      self._item[self._top] = value	
  # 彈出資料
  def pop(self):
    if not self.isEmpty():
      popped = self._item[self._top]
      self._top -= 1
      return popped
    return None
  #查看頂端資料
  def peek(self):
    if not self.isEmpty():
      return self._item[self._top]
    return None
  #印出資料
  def print(self):		#bottom up
    for i in range(self._top+1):
      print(self._item[i], end = ' ')
    print()
  
def main():
  a = Stack()
  print(a.isEmpty())
  a.push(4)
  a.push(5)
  print(a.pop())
  a.print()

if __name__ == '__main__':
  main()