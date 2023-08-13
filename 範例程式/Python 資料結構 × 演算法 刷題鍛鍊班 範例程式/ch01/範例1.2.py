sum = 0
termi = 1
x = 1.4
for i in range(0, 6): # i 的範圍是從 0 到 5
  sum += termi
  termi = termi * x/2
print(sum)