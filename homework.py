name = input("請輸入姓名：")
years = input("請輸入年齡：")
year = int(years)
workyears = 60 - year
if year >= 65:
    print('您的年齡已達退休年齡')
else:
    print(f'姓名', name, '還有', workyears, '年退休')
