import sys

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1  # start point
for i in range(n): 
    for j in range(n): 
        move = board[i][j]
        if move:  # if move == 0, destination
            if i + move < n: 
                dp[i+move][j] += dp[i][j]
            if j + move < n: 
                dp[i][j+move] += dp[i][j]
print(dp[n-1][n-1])
