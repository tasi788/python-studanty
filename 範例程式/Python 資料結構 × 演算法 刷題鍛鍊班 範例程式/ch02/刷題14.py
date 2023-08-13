from math import inf
def packing(packages, boxes):
  min_waste = inf # 最大數
  supFound = False
  for s in range(len(boxes)): # supplier，供應商 s
    cur_waste = 0 # 供應商 s 的總浪費空間
    p = 0 # 第 p 個商品，從第 0 個商品裝箱
    b = 0 # 第 b 種箱子，從第 0 種箱子裝箱
    while b < len(boxes[s]): # 還有箱子可裝箱
      while packages[p] <= boxes[s][b]: # 裝得下
        cur_waste += boxes[s][b] - packages[p] # 加總其空間浪費
        p += 1 # 裝下一個商品
        if p >= len(packages): # 商品都已裝箱
          min_waste = min(cur_waste, min_waste) # 必要時更新最小值
          supFound = True # 有供應商可完全裝箱
          break
      b += 1 # 試下一種箱子
      if p >= len(packages): # 商品都已裝箱，無須試下一種箱子
        break
  if supFound:
    return min_waste
  return -1

packages = list(map(int, input().split()))
packages.sort()
m = int(input())  #供應商數量
boxes = [[] for _ in range(m)]
for s in range(m): #每一個供應商提供的箱子種類
  boxes[s] = list(map(int, input().split()))
  boxes[s].sort()
print(packing(packages, boxes))
#輸入範例
#2 3 5
#2
#4 8
#8 2
#輸出 6