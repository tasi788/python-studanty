from stackClass import *
priority = {'(':0, '+':1,'-':1,'*':2,'/':2}
def operands(ch): #假設運算元為單一字母
  if ch.isalpha():
    return True
  return False
def in_to_post(infix):
  myStack = Stack()
  postfix = []
  for token in infix:	    #中序式尚未讀完，重複迴圈
    if operands(token):		#規則2. 運算元直接輸出至後序式
      postfix.append(token)
    elif token == '(':		#堆疊規則1. ‘(’ 一律Push
      myStack.push(token)
    elif token == ')':    #堆疊規則2. 一直Pop直到‘(’一同抵銷
      while not myStack.isEmpty():
        element = myStack.pop()
        if element == '(':
          break
        postfix.append(element)
    elif token in priority:	#堆疊規則3. 比較優先序
      while not myStack.isEmpty():
        element = myStack.peek()
        if priority[token] <= priority[element]:
          element = myStack.pop()
          postfix.append(element)
        else:
          break
      myStack.push(token)
  while not myStack.isEmpty(): #規則4. 將堆疊中剩餘的運算子依序Pop到後序式
    element = myStack.pop()
    postfix.append(element)
  return postfix

in_str = input()
print("".join(in_to_post(in_str)))