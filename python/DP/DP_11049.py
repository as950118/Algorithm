import sys
sys.setrecursionlimit(100000)

ret = 0
temp = 0
n = int(input())
arr = [[0]*(2) for i in range(n+1)]
dp = [[0]*(n+1) for i in range(n+1)]
for i in range(n):
	arr[i+1] = list(map(int, sys.stdin.readline().split()))

def func(l, r):
	if dp[l][r]>0:
		return dp[l][r]
	if l==r-1:
		dp[l][r] = arr[l][0] * arr[l][1] * arr[r][1]
		return dp[l][r]
	if l==r:
		dp[l][r] = 0
		return 0

	dp[l][r] = func(l+1,r) + arr[l][0]*arr[l][1]*arr[r][1]

	for i in range(l+1, r):
		dp[l][r] = min(func(l,i) + func(i+1,r) + arr[l][0]*arr[i][1]*arr[r][1], dp[l][r])
	return dp[l][r]

func(1,n)
print(dp[1][n])
