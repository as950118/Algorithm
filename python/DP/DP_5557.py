import sys
sys.setrecursionlimit(1000000000)
from collections import deque

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.insert(0,0)
dp = [[-1]*(21) for i in range((n+1))]


def func(cur, val):
    if cur == n:
        if val == arr[cur]:
            return 1
        else:
            return 0
    if dp[cur][val] != -1:
        return dp[cur][val]
    temp = 0
    if val - arr[cur] >= 0:
        temp += func(cur+1, val - arr[cur])
    if val + arr[cur] <= 20:
        temp += func(cur+1, val + arr[cur])
    dp[cur][val] = temp

    return dp[cur][val]

print(func(2,arr[1]))
