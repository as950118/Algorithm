import sys
sys.setrecursionlimit(1000000000)
from collections import deque

arr1 = list(input())
arr2 = list(input())
len1 = len(arr1)
len2 = len(arr2)
dp = [[0]*(len2+1) for i in range(len1+1)]
strdp = [[""]*(len2+1) for i in range(len1+1)]
arr1.insert(0,0)
arr2.insert(0,"")
for i in range(1, len1+1):
	for j in range(1, len2+1):
		if arr1[i] == arr2[j]:
			dp[i][j] = dp[i-1][j-1] + 1
			strdp[i][j] = strdp[i-1][j-1] + arr1[i]
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			if dp[i-1][j] >= dp[i][j-1]:
				strdp[i][j] = strdp[i-1][j]
			else:
				strdp[i][j] = strdp[i][j-1]
print(dp[len1][len2])
print(strdp[len1][len2])
