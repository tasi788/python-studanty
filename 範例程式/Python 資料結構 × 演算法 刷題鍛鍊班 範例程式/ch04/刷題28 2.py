from stackClass import *
def palindrome(str):
  myStack = Stack()
  for ch in str:
    myStack.push(ch)  
  for ch in str:
    if myStack.pop() != ch:
      return False
  return True
in_word = list(input()) 
print(palindrome(in_word))