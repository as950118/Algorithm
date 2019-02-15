import sys
from collections import deque
sys.setrecursionlimit(1000000000)

n = int(input())
arr = deque()
dp = deque([[-1]*n for i in range(n)])
for i in range(n):
    arr.append(list(map(int, input().split())))


def func(i, j):
    if i==n-1 and j==n-1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0

    nx = i + arr[i][j]
    if nx<n:
        dp[i][j] += func(nx, j)
    ny = j + arr[i][j]
    if ny<n:
        dp[i][j] += func(i,ny)
    return dp[i][j]
print(func(0,0))
