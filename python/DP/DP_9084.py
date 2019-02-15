import sys
sys.setrecursionlimit(1000000000)
from collections import deque

t = int(input())

def func(a,b):
    if a == m:
        return 1
    if dp[a][b] != -1:
        return dp[a][b]
    dp[a][b] = 0
    for i in range(b, n):
        if a+arr[i] <= m:
            dp[a][b] += func(a+arr[i], i)

    return dp[a][b]

for T in range(t):
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    dp = [[-1]*(n) for i in range(m+1)]
    print(func(0, 0))
