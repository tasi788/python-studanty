#!/usr/bin/env python3
# 本程式內容為輸入姓名及年齡後進行法定退休年齡自動計算

import time as t   #載入time模組，並取名為t

print('本程式內容為輸入姓名及年齡後進行法定退休年齡自動計算')
workyears = 65    # 設定法定退休年齡
name = input('請輸入姓名:')
# 要求輸入年齡的資料必須為數字，若不是數字則返回要求重新輸入年齡
while True:
    try:
        age = int(input('請輸入年齡:'))
        break
    except ValueError:
        print('請重新輸入正確數值，年齡需為數字')
# 設定目前年齡若大於等於法定退休年齡直接顯示已達退休年齡，若未達法定退休年齡則顯示計算後年數
def numbers(years):
    if age >= workyears:
        print('您的年齡已達退休年齡')
    else:
        print(f'姓名', name, '還有', workyears - years, '年退休')
Value = numbers(age)

print('【5秒後自動退出程式】')
t.sleep(5)    # 停留5秒後退出程式