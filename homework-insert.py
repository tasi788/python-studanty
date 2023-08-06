#!/usr/bin/env python3

print('本程式示範由LIST最後三組字串搬移至LIST最前方')
# 定義X為十組字串的LIST
x = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10']

n = 3    # 設定搬移字串數目
while n > 0:
    y = x[-1]    # 設定y為X LIST最後一個字串   
    x.insert(0, y)    # 將y插入X LIST的最前端
    del x[-1]    # 刪除X LIST最後一個字串
    n = n - 1

print(x)    # 顯示搬移完成厚的成果
