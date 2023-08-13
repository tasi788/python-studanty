from stackClass import *
def checkSequence(pushed, popped):
  j = 0
  myStack = Stack()
  for i in range(len(popped)):
    x = popped[i]
    while j < len(pushed) and x not in myStack.item:
      myStack.push(pushed[j])
      j += 1
    if myStack.pop() != x:
        return False
  return True

list1 = list(input().split())
list2 = list(input().split()) 
print(checkSequence(list1, list2))