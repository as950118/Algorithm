import sys
sys.setrecursionlimit(1000000)

n = sys.stdin.readline()
n = int(n)
dp = [0]*(4)
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
	dp[3] = dp[2] + dp[1]
	dp[0] = dp[1]
	dp[1] = dp[2]
	dp[2] = dp[3]
	for j in range(4):
		if dp[j]>=15746:
			dp[j] = dp[j]%15746

print(dp[3])

'''
1
2
3
5
8 00001 00100 10000 00111 11100 10011 11001 11111

'''
