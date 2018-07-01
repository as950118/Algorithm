import sys
sys.setrecursionlimit(1000000000)

n , m = input().split()
n = int(n)
m = int(m)
arr = [[0]*m for i in range(n)]
dp = [[[0]*m for i in range(m)] for j in range(n)]
for i in range(0, n):
    arr[i] = input().split()
    for j in range(0, m):
        arr[i][j] = int(arr[i][j])
        dp[i][j][j] = arr[i][j]

k = int(input())
for a in range(0, k):
    i,j , x,y = input().split()
    i = int(i)-1
    j = int(j)-1
    x = int(x)-1
    y = int(y)-1
    i = min(i,x)
    x = max(i,x)
    j = min(j,y)
    y = max(j,y)
    ret = 0
    for _x in range(i, x+1):
        for _y in range(j, y+1):
            dp[_x][j][_y] = dp[_x][j][_y-1] + arr[_x][_y]
        ret += dp[_x][j][_y]
    print(ret)
