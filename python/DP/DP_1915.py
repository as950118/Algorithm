import sys
import math
from collections import deque

sys.setrecursionlimit(1000000000)



m,n = map(int, input().split())
arr = [[0]*(n+1) for i in range(m+1)]

for i in range(1, m+1):
	temp = input()
	for j in range(1, n+1):
		arr[i][j] = int(temp[j-1])
ret = 0

dp = [[0]*(n+1) for i in range(m+1)]

for i in range(1, m+1):
	for j in range(1, n+1):
		if arr[i][j] == 1:
			dp[i][j] = 1
			temp = min(dp[i-1][j], dp[i][j-1])
			if dp[i-temp][j-temp] != 0:
				dp[i][j] = temp + 1
			else:
				dp[i][j] = temp
			ret = max(dp[i][j], ret)
'''
for i in range(1, m+1):
	print(arr[i], dp[i])
'''
print(ret*ret)
