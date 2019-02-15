import sys
sys.setrecursionlimit(1000000000)
from collections import deque

n, s, m = map(int, sys.stdin.readline().split())
arr = [-1]*(n)
dp = [[-1]*(m+1) for i in range(n+1)]
arr = list(map(int, sys.stdin.readline().split()))

ret = -1
dp[0][s] = 1
for i in range(n):
    for j in range(0, m+1):
        if dp[i][j] == 1:
            if j-arr[i] >= 0:
                dp[i+1][j-arr[i]] = 1
            if j+arr[i] <= m:
                dp[i+1][j+arr[i]] = 1

for i in range(m, 0-1, -1):
    if dp[n][i] == 1:
        ret = i
        break
print(ret)
