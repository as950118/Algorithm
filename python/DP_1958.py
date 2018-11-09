import sys

Arr1 = list(input())
Arr2 = list(input())
Arr3 = list(input())

def func(arr1, arr2,arr3):
	len1 = len(arr1)
	len2 = len(arr2)
	len3 = len(arr3)
	dp = [[[(0) for i in range(len3+1)] for iii in range(len2+1)] for iii in range(len1+1)]
	ret = 0
	for i in range(1,len1+1):
		for j in range(1,len2+1):
			for k in range(1, len3+1):
				if arr1[i-1] == arr2[j-1] == arr3[k-1]:
					dp[i][j][k] = dp[i-1][j-1][k-1] + 1
				else:
					dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

	return dp[len1][len2][len3]

print(func(Arr1,Arr2,Arr3))
