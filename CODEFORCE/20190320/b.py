import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = list(map(int, input().split()))
dp = [0 for i in range(n)]
def func(cur):
    if arr[cur] == 1:
        if cur==n-1:
            dp[cur] = 1
            dp[cur] += dp[0]
        else:
            dp[cur] = 1
            dp[cur] += func(cur+1)
    else:
        if cur==n-1:
            return dp[cur]
        func(cur+1)
    return dp[cur]
func(0)
print(max(dp))
