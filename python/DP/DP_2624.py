import sys

t = int(sys.stdin.readline())
k = int(sys.stdin.readline())
p = [(0) for i in range(k)]
n = [(0) for i in range(k)]

dp = [[(-1) for i in range(k)] for ii in range(t+1)]

for i in range(k):
	p[i], n[i] = map(int, sys.stdin.readline().split())

def func(cur, idx):
	if cur==t:
		return 1
	if idx==k:
		return 0
	if dp[cur][idx] != -1:
		return dp[cur][idx]

	dp[cur][idx] = 0
	for i in range(n[idx]+1):
		if cur+p[idx]*(i)>t:
			continue
		dp[cur][idx] += func(cur+p[idx]*(i), idx+1)
	return dp[cur][idx]
print(func(0,0))
