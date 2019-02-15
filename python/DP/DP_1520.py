import sys
sys.setrecursionlimit(1000000000)
from collections import deque

m, n = map(int, sys.stdin.readline().split())
#arr = [[0]*n for i in range(m)]
#dp = [[0]*n for i in range(m)]
arr = deque([[0]*(n) for i in range(m)])
dp = deque([-1]*(n) for i in range(m))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(m):
    #arr[i] = list(map(int, input().split()))
    arr[i] = deque(list(map(int, input().split())))


def func(i, j):
    if i==m-1 and j==n-1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 0

    for a in range(4):
        nx = dx[a] + i
        ny = dy[a] + j
        if 0 <= nx and nx < m and 0 <= ny and ny < n:
            if arr[i][j] > arr[nx][ny]:
                dp[i][j] += func(nx, ny)
    return dp[i][j]
print(func(0,0))
