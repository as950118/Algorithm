import sys
sys.setrecursionlimit(1000000000)
from collections import deque

n = int(input())
arr = deque([0]*(n+1))
dp = deque([0]*(n+1))
arr = deque(list(map(int, input().split())))
arr.appendleft(0)
ret = 0

def func(n, i):
    global ret
    if n<i:
        return 0
    dp[i] = 1;
    for j in range(1, i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    ret = max(ret, dp[i])
    func(n, i+1)

func(n,0)
print(ret)
