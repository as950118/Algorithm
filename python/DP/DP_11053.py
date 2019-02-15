import sys
sys.setrecursionlimit(1000000000)
from collections import deque

n = int(sys.stdin.readline())
arr = deque(map(int, sys.stdin.readline().split()))
arr.appendleft(0)

dp = deque([0]*(n+1))

ret = 0

def func(i):
    global ret
    if n<i:
        return 0
    dp[i] = 1

    for j in range(1,i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
    func(i+1)

    ret = max(ret, dp[i])
    return ret
print(func(1))
