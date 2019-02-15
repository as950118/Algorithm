import sys


n,l,r = map(int, sys.stdin.readline().split())
dp = [[[0 for i in range(n+1)] for ii in range(n+1)] for iii in range(n+1)]
mod = 1000000007

for i in range(1,n+1):
	dp[i][i][1] = 1
	dp[i][1][i] = 1

for i in range(2,n+1):
	for j in range(1,l+1):
		for k in range(1,r+1):
			dp[i][j][k] = (dp[i-1][j][k]*(i-2) + dp[i-1][j-1][k] + dp[i-1][j][k-1])%mod
print(dp[n][l][r])
