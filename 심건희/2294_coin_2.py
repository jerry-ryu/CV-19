import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
min_coin = 100000
for i in range(n):
    coins.append(int(sys.stdin.readline()))
    min_coin = min(min_coin, coins[i])
if min_coin > k: 
    print(-1)
else: 
    dp = [-1] * (k+1)
    dp[0], dp[min_coin] = 0, 1
    for i in range(min_coin+1, k+1): 
        for j in range(len(coins)): 
            coin = coins[j]
            if i - coin >= 0 and dp[i-coin] != -1: 
                if dp[i] == -1:  # first
                    dp[i] = dp[i-coin] + 1
                else: 
                    dp[i] = min(dp[i], dp[i-coin] + 1)
    print(dp[k])
