import sys
from collections import deque
sys.setrecursionlimit(1000000000)


N = int(input())

arr = deque(list(map(int, input().split())))
arr.appendleft(0)
dp = deque([0])
ret = 0
for i in range(1, N+1):
    dp.append(1)
    for j in range(1, i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
    ret = max(ret, dp[i])

print(ret)
