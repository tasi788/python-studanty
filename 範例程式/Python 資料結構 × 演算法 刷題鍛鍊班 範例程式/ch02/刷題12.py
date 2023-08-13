def findCoins(n):
  coins = [50, 10, 5, 1]
  count = 0
  for i in range(len(coins)):	
    count += n // coins[i]
    n = n % coins[i]
  return count

n = int(input())				
print(findCoins(n))