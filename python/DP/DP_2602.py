import sys

dir = input()
arr = ["" for i in range(3)]
arr[1] = input()
arr[2] = input()
n = len(dir)
m = len(arr[1])

dp = [[[(-1) for i in range(n)] for ii in range(m)] for iii in range(3)]

def func(x, cur, y):
	if y == n:
		return 1
	if cur == m:
		return 0
	if dp[x][cur][y] != -1:
		return dp[x][cur][y]
	dp[x][cur][y] = 0
	for i in range(cur, m):
		if arr[x][i] == dir[y]:
			dp[x][cur][y] += func(x^3, i+1, y+1)
	return dp[x][cur][y]

print(func(1,0,0)+func(2,0,0))
