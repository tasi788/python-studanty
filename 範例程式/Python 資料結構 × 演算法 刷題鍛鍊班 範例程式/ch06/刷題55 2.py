from BSTClass import *
from BST_IteratorClass import *
t = BST()
t.createFromFile('bst6-28.txt')
t.inorder(t.root)
print()
obj = BST_Iterator(t.root)
minDiff = float('inf')
prev = 0
while obj.hasNext():
  current = int(obj.next())
  minDiff = min(minDiff, current-prev)
  prev = current
  #print(current)
print(minDiff)