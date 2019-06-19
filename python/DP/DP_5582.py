import sys
sys.setrecursionlimit(1000000000)
from collections import deque

arr1 = deque(sys.stdin.readline())
arr2 = deque(sys.stdin.readline())
arr1.pop()
arr2.pop()

len1 = len(arr1)
len2 = len(arr2)

dp = [[0]*(len2+1) for i in range(3)]
ret = 0

for i in range(1,len1+1):
	for j in range(1,len2+1):
		if arr1[i-1] == arr2[j-1]:
			dp[2][j]=dp[1][j-1]+1
			if dp[2][j]>ret:
				ret=dp[2][j]
		else:
			dp[2][j]=0
	dp[1]=dp[2][:]
print(ret)
