name = input('請輸入姓名：')
year = int(input('請輸入年齡'))

workyears = 60 - year

if year >= 65:
    print('您的年齡已達退休年齡')
else:
    print(f'姓名', name, '還有', workyears, '年退休')
