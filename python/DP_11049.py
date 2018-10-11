import sys
sys.setrecursionlimit(1000000000)
from collections import deque

n = int(sys.stdin.readline())
dp = [[-1]*(n+1) for i in range(n+1)]
arr = [[-1]*(2) for i in range(n+1)]
for i in range(n):
    arr[i+1] = list(map(int, sys.stdin.readline().split()))


def func(l, r):
    if l == r-1:
        dp[l][r] = arr[l][0] * arr[l][1] * arr[r][1]
        return dp[l][r]
    if l == r:
        return 0
    if dp[l][r] != -1:
        return dp[l][r]

    dp[l][r] = 1

    for i in range(l, r):
        dp[l][r] = min(func(l, i) + func(i+1, r) + (arr[l][0] * arr[i][1] * arr[r][1]), dp[l][r])

    return dp[l][r]


func(1,n)
print(dp[1][n-1]*arr[1][1], dp)
