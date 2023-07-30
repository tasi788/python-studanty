name = input('請輸入姓名：')
age = int(input('請輸入年齡'))

years = 60 - age

if age >= 65:
    print('您的年齡已達退休年齡')
else:
    print(f'姓名', name, '還有', years, '年退休')
