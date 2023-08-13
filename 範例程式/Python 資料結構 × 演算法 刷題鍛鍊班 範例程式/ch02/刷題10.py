from math import ceil
def findPrime(n):			# 進階版
  prime = [True]*n
  for i in range(2, ceil(n**0.5)):
     if prime[i] == True:
        for j in range(i*i, n, i): 
          prime[j] = False
  return prime
def findPrime_Old(n):
  prime = [True]*n			#產生陣列
  for i in range(2, n):
    if prime[i] == True:		#若i是質數
      for j in range(i+1, n):
        if (j % i) == 0:			#檢查i+1 ~ n 每一個數是否為i的倍數
           prime[j] = False
  return prime	  		

n = int(input())
primes = findPrime(n)
for i in range(2, n):
  if primes[i]:
    print(i, end = " ")