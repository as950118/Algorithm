import sys
sys.setrecursionlimit(1000000000)
debug = 1
while debug:
    n, m = input().split()
    n = int(n)
    m = int(m)
    arr = [[0]*m for i in range(n)]
    dp = [[0]*m for i in range(n)]
    for i in range(0, n):
        arr[i] = input().split()
        for j in range(0, m):
            arr[i][j] = int(arr[i][j])

    dp[0][0] = arr[0][0]
    for i in range(1, m):
        dp[0][i] = dp[0][i-1] + arr[0][i]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + arr[i][0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])+ arr[i][j]
    print(dp[n-1][m-1])
    debug = 0
