import sys
sys.setrecursionlimit(10**8)
inf = sys.maxsize

n = int(input())
dp = [inf for i in range(n+1)]
dp[1] = 0
def func(i):
    if dp[i] != inf:
        return dp[i]
    dp[i] = func(i-1)+1
    if i%2 == 0:
        dp[i] = min(dp[i], func(i//2)+1)
    if i%3 == 0:
        dp[i] = min(dp[i], func(i//3)+1)
    return dp[i]
print(func(n))
