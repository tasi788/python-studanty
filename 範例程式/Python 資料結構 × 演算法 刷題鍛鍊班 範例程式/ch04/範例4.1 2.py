from stackClass import *
in_word = list(input())  #輸入字串，拆成字元放入in_word
myStack = Stack()
for ch in in_word:
  myStack.push(ch)    #推入堆疊
while not myStack.isEmpty():
  print(myStack.pop(), end = '')  #彈出堆疊
