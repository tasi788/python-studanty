sum = 0
termi = 1
A = ["好吃的", "好看的", "好玩的"]
B = ["蘋果", "手機"]
for adj in A:
  for noun in B:
    print(adj, noun)
print()
for noun in B:
  for adj in A:
    print(adj, noun)