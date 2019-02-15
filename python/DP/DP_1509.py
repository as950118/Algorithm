import sys
sys.setrecursionlimit(1000000000)

arr = sys.stdin.readline()
n = len(arr)-1
chk = [[0]*(n) for i in range(n)]
dp = [0]*(n)

for i in range(n):
    for j in range(n-i):
        if i == 0:
            chk[j][j] = 1
            continue
        k = i+j
        if arr[j] == arr[k] and (chk[j+1][k-1] or j==k-1):
            chk[j][k] = 1


for i in range(n):
	for j in range(i+1):
		if chk[j][i]:
			if dp[i] == 0 or dp[i]>dp[j-1]+1:
				dp[i] = dp[j-1]+1
print(dp[n-1])
