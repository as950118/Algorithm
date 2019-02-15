import sys

n = int(sys.stdin.readline())
arr = [0]+ list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

dp = [[(0) for i in range(n+1)] for i in range(4)]
ret=0

arr_sum = [(0) for i in range(n+1)]
for i in range(n):
	arr_sum[i+1] = arr_sum[i] + arr[i+1]

for i in range(1,4):
	for j in range(i*m, n+1):
		dp[i][j] = max(dp[i][j-1], dp[i-1][j-m] + arr_sum[j]-arr_sum[j-m])
		ret = max(ret, dp[i][j])
print(ret)
