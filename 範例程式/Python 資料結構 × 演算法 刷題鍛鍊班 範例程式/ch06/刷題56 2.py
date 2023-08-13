from BSTClass import *
t = BST()
t.createFromFile('bst6-28.txt')
t.inorder(t.root)
print()
k = int(input())
nums = map(int, t.nodes)
for num in nums:
  if t.search(str(k-num)):
    print(num, k-num)
    break
else:
  print("No answer")