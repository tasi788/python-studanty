def	palindrome(s):	#假設s=903
  left = 0			# left = 0, s[0]=’9’
  right = len(s)-1		# right = 2, s[2]=’3’
  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True

s = input()
print(palindrome(s))