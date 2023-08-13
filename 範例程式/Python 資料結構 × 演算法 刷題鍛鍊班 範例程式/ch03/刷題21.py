import string
def columnEncode(n):
  Title = ''
  while n>0:
    y = (n-1) % 26
    n = (n-1)//26
    Title = chr(y+ord('A')) + Title
  return Title
def convertToTitle(n):  #字典版
  ord = dict((index,value) for index, value in \
      enumerate(string.ascii_uppercase))
  Title = ""
  while n>0:
    y = (n-1) % 26
    n = (n-1)//26
    Title = ord[y] + Title
  return Title
  
print(702, convertToTitle(702))
print(702, columnEncode(702))
print(2147483647, convertToTitle(2147483647))
print(2147483647, columnEncode(2147483647))