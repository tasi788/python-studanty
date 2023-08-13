import openpyxl

# 讀取 Excel 檔案，注意填寫正確的檔案路徑
wb = openpyxl.load_workbook('names_and_savings.xlsx')

# 選取要讀取的工作表，注意填寫正確的工作表名稱
sheet = wb['工作表1']

# 假設資料位於第一列，使用 list comprehension 將資料轉換成 list
first_name_list = [cell.value for cell in sheet['A']]

print(first_name_list)
print(len(first_name_list))
