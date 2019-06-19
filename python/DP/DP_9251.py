import sys
sys.setrecursionlimit(1000000000)
from collections import deque

arr1 = list(input())
arr2 = list(input())
len1 = len(arr1)
len2 = len(arr2)
dp = [[0]*(len2+1) for i in range(len1+1)]
strdp = [[]]
arr1.insert(0,0)
arr2.insert(0,0)
for i in range(1, len1+1):
	for j in range(1, len2+1):
		if arr1[i] == arr2[j]:
			dp[i][j] = dp[i-1][j-1] + 1
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len1][len2])
