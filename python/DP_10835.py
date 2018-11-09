import sys
from collections import deque
sys.setrecursionlimit(1000000000)


n = int(sys.stdin.readline())

arr1 = deque(map(int, sys.stdin.readline().split()))
arr2 = deque(map(int, sys.stdin.readline().split()))

dp = [[-1]*(n) for i in range(n)]

def func(a,b):
    if a>n-1 or b>n-1:
        return 0
    if dp[a][b] != -1:
        return dp[a][b]
    if arr1[a] > arr2[b]:
        dp[a][b]= func(a, b+1) + arr2[b]
    else:
        dp[a][b] = max(func(a+1,b+1),func(a+1,b))
    return dp[a][b]

print(func(0,0))
