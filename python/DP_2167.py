import sys
sys.setrecursionlimit(1000000000)

n, m = map(int, sys.stdin.readline().split())
arr2 = [[0]*(m+1) for i in range(n+1)]
arr = [[0]*(m+1) for i in range(n+1)]
dp = [[0]*(m+1) for i in range(n+1)]
for i in range(1, n+1):
    arr2[i] = input().split()
    for j in range(1,m+1):
        arr[i][j] = int(arr2[i][j-1])
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + arr[i][j] - dp[i-1][j-1]

k = int(input())
for a in range(0, k):
    i,j, x,y = map(int, sys.stdin.readline().split())
    if i==x and j==y:
        print(arr[i][j])
    else:
        print(dp[x][y] - (dp[i-1][y] + (dp[x][j-1] - dp[i-1][j-1])))
