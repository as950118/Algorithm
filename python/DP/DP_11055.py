import sys
sys.setrecursionlimit(1000000000)
from collections import deque


def func(n, i):
    global ret
    if n<i:
        return 0
    if arr[i]>arr[i-1]:
        #dp[i] = dp[i-1]+arr[i]
        dp.append(dp[i-1]+arr[i])
    else:
        #dp[i] = arr[i]
        dp.append(arr[i])
    for j in range(1, i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])
    ret = max(ret, dp[i])
    func(n, i+1)
ret=0
N = int(input())
dp = deque([0])
arr = deque(list(map(int, input().split())))
arr.appendleft(0)
'''
dp = [0]*(N+1)
arr =  list(map(int, input().split()))
arr.insert(0, 0)
'''
func(N, 1)
print(ret)
