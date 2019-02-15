import sys
sys.setrecursionlimit(1000000000)
from collections import deque

n, m, k = map(int ,sys.stdin.readline().split())
dp = [[-1]*(m+1) for i in range(n+1)]
share = k//(m) + 1
rest = k%(m)
dir_x = [-1,0]
dir_y = [0,-1]
def func(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for dir in range(2):
        if x+dir_x[dir]==1 and y+dir_y[dir]==1:
            dp[share][rest] += dp[x][y]
        elif x+dir_x[dir]>0 and y+dir_y[dir]>0:
            temp = 1
            temp += func(x+dir_x[dir], y+dir_y[dir])
            dp[x][y] = max(temp, dp[x][y])
    return dp[x][y]
def func2(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for dir in range(2):
        if x+dir_x[dir]==share and y+dir_y[dir]==rest:
            dp[n][m] += dp[x][y]
        elif x+dir_x[dir]>share-1 and y+dir_y[dir]>rest-1:
            temp = 1
            temp += func2(x+dir_x[dir], y+dir_y[dir])
            dp[x][y] = max(temp, dp[x][y])
    return dp[x][y]

a=func(share,rest)
b=func2(n,m)
print(a,b,a*b)
for i in range(n+1):
    print(dp[i])
