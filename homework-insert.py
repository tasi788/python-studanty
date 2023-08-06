#!/usr/bin/env python3

import time as t    # 載入time模組，並取名為t
print('本程式示範由LIST最後三組字串搬移至LIST最前方')
# 定義X為十組字串的LIST
x = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10']

print(x)    # 畫面顯示X LIST資料
print('目前顯示LIST為X原始資料')

# 輸入需求搬移字串的數量，要求輸入搬移字串數目的資料必須為數字，若不是數字則返回要求重新輸入年齡
while True:
    try:
        n = int(input('請輸入搬移字串數量:(1-9)'))
        if n < 10:
            break
        else:
            print('輸入數字錯誤，請重新輸入數字(1-9)')
            print('或按下CTRL+C退出程式')
    except ValueError:
        print('請輸入數字(1-9),不接受數字以外輸入')
        print('或按下CTRL+C退出程式')
        continue

while n > 0:
    y = x[-1]    # 設定y為X LIST最後一個字串   
    x.insert(0, y)    # 將y插入X LIST的最前端
    del x[-1]    # 刪除X LIST最後一個字串
    n = n - 1

print(x)    # 顯示搬移完成厚的成果
print('目前顯示LIST為X搬移字串後資料')

print('【5秒後自動退出程式】')
t.sleep(5)    # 停留5秒後結束程式
