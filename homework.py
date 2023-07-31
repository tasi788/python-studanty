name = input('請輸入姓名:')
age = int(input('請輸入年齡:'))
workyears = 65      #法定退休年齡
years = workyears - age     #自動減去退休年齡

if age >= workyears:    #限定年齡大於65歲自動顯示已退休
    print('您的年齡已達退休年齡')
else:
    print(f'姓名', name, '還有', years, '年退休')