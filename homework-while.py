#!/usr/bin/env python3
# 本檔案內容為輸入姓名及年齡後進行法定退休年齡自動計算

import sys    #載入sys

name = input('請輸入姓名:')

age = 0    #提前定義age參數為數字
# 要求輸入年齡的資料必須為數字，若不是數字則返回要求重新輸入年齡
while True:
    try:
        age = int(input('請輸入年齡:'))
        break
    except ValueError:
        print('請輸入正確數值')

workyears = 65    #設定法定退休年齡
years = workyears - age    #法定退休年齡減去目前年齡

# 設定目前年齡若大於等於法定退休年齡直接顯示已達退休年齡，若未達法定退休年齡則顯示計算後年數
if age >= workyears:
    print('您的年齡已達退休年齡')
else:
    print(f'姓名', name, '還有', years, '年退休')