#!/usr/bin/env python3

x = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10']

n = 3
while n > 0:
    y = x[-1]
    x.insert(0, y)
    del x[-1]
    n = n - 1

print(x)
