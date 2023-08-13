def longestSub(chars):
  pos = {}
  maxLen, curLen, curStart = 0, 0, 0
  for i in range(len(chars)):
    ch = chars[i]
    if ch in pos and pos[ch] >= curStart: #出現過且在目前序列中
      curStart = pos[ch] + 1
      curLen = i - curStart + 1
    else:
      curLen += 1
    maxLen = max(maxLen, curLen) 
    pos[ch] = i  
  return maxLen

strIn = list(input())
print(longestSub(strIn))
#輸入 fsfetwenwe
#輸出 5