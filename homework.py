name = input('請輸入姓名:')
age = int(input('請輸入年齡:'))
workyears = 65      #法定退休年齡
years = workyears - age     #法定退休年齡減去目前年齡

if age >= workyears:    #設定目前年齡若大於等於法定退休年齡直接顯示已達退休年齡，若未達法定退休年齡則顯示計算後年數
    print('您的年齡已達退休年齡')
else:
    print(f'姓名', name, '還有', years, '年退休')