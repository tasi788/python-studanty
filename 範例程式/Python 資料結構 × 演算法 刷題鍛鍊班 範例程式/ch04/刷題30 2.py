from stackClass import *
def checkBracket(str):
  bracket = {'(':')', '[':']', '{':'}'}
  myStack = Stack()
  for ch in str:
    if ch in bracket:
      myStack.push(bracket[ch])
    else:
      if myStack.pop() != ch:
        return False
  if not myStack.isEmpty():
    return False
  return True

in_word = list(input()) 
print(checkBracket(in_word))