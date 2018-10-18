import sys
sys.setrecursionlimit(1000000)


n ,m = map(int, sys.stdin.readline().split())
arr = [[0]*(m) for i in range(n)]
dp = [[-10000000]*(m) for i in range(n)]
dir_x = [1,-1,0]
dir_y = [0,0,1]

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

dp[0][0] = arr[0][0]

for i in range(1, m):
    dp[0][i] = arr[0][i] + dp[0][i-1]


def func(cx, cy):
    if cy == 0:
        dp[cx][cy] = arr[cx][cy] + max(dp[cx-1][cy], dp[cx][cy+1])
    elif cy == m-1:
        dp[cx][cy] = arr[cx][cy] + max(dp[cx-1][cy], dp[cx][cy-1])
    else:
        dp[cx][cy] = arr[cx][cy] + max(dp[cx-1][cy], dp[cx][cy-1], dp[cx][cy+1])


for i in range(1,n):
    for j in range(m):
        func(i,j)

print(dp[n-1][m-1])
for i in range(n):
    print(dp[i])
