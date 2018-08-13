import sys
sys.setrecursionlimit(1000000)

t = sys.stdin.readline()
t = int(t)
for T in range(t):
	n = sys.stdin.readline()
	n = int(n)
	dp = [0]*(5)
	dp[0] = 1
	dp[1] = 1
	dp[2] = 2
	dp[3] = 4
	if n>3:

		for i in range(4, n+1):
			dp[4] = dp[3] + dp[2] + dp[1] + dp[0]
			for j in range(4):
				dp[j] = dp[j+1]


		print(dp[4])
	else:
		print(dp[n])
