#!/usr/bin/env python3

print ('hello, world')
print ('I\'m DAST')
      
n = 9
r = 1
while n > 0:
    r = r * n
    n = n - 1
print(r)

input = input('請輸入圓半徑數值:')
radius = float(input)
PI = 3.14
print('圓半徑：', radius)
print('圓周長：', 2 * PI * radius)
print('圓面積：', PI * radius * radius)
