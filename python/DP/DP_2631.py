import sys
sys.setrecursionlimit(1000000000)
from collections import deque

n = int(input())
arr = [int(input()) for i in range(n)]
dp = [-1]*(n)
def func(start):
    if dp[start] != -1:
        return dp[start]
    dp[start] = 0
    for i in range(start+1, n):
        if arr[start] < arr[i]:
            temp = 1
            temp += func(i)
            dp[start] = max(dp[start], temp)
    return dp[start]
for i in range(n):
    func(i)
print(len(arr)-max(dp)-1)
