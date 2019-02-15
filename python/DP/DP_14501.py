import sys
sys.setrecursionlimit(1000000000)
from collections import deque

n = int(input())
arr_t = deque([0])
arr_p = deque([0])
dp = [0]*(n+1)
for i in range(n):
    t, p = input().split()
    arr_t.append(int(t))
    arr_p.append(int(p))

def func(i):
    if i>n:
        return 0
    if i+arr_t[i]-1 <= n:
        dp[i+arr_t[i]-1] = max(dp[i+arr_t[i]-1], dp[i-1] + arr_p[i])
    dp[i] = max(dp[:i+1])
    func(i+1)
func(1)
print(dp[n])
