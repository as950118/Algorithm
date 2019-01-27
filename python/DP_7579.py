MAX = 10000001
n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
dp = [[-1 for i in range(n)] for i in range(m)]
print(dp)
def func(cur, idx):
    if dp[cur][idx] != -1:
        return dp[cur][idx]
    if idx==n:
        dp[cur][idx] = 0
        return 0
    if cur < cost[idx]:
        dp[cur][idx] = func(cur, idx+1)
        return dp[cur][idx]
    if cur >= cost[idx]:
        dp[cur][idx] = max( func(cur,idx+1), func(cur-cost[idx], idx+1)+memory[idx] )
        return dp[cur][idx]

for i in range(n):
    if func(cost[i], 0) >= m:
        print(i)
        break
