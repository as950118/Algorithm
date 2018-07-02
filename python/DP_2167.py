import sys
sys.setrecursionlimit(1000000000)

def func(i,x , j,y, ret):
    for _x in range(i-1, x):
        for _y in range(0, y):
            if dp[_x][_y] == 0:
                dp[_x][_y] = dp[_x][_y-1] + arr[_x][_y]
        if j==1:
            ret += dp[_x][y-1]
        else:
            ret += dp[_x][y-1] - dp[_x][j-2]
    return ret

n, m = input().split()
n = int(n)
m = int(m)
arr = [[0]*m for i in range(n)]
dp = [[0]*m for i in range(n)]
for i in range(0, n):
    arr[i] = input().split()
    for j in range(0, m):
        arr[i][j] = int(arr[i][j])
    dp[i][0] = arr[i][0]

k = int(input())
for a in range(0, k):
    i,j , x,y = input().split()
    i = int(i)
    j = int(j)
    x = int(x)
    y = int(y)
    if i==x and j==y:
        print(arr[i-1][j-1])
    else:
        print(func(i,x , j,y, 0))
