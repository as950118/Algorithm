import sys
sys.setrecursionlimit(1000000)

MIN = -1000000

n ,m = map(int, sys.stdin.readline().split())
arr = [[0]*(m) for i in range(n)]
dp = [[[MIN]*4 for j in range(m)] for k in range(n)]
dir_x = [0,1,0]
dir_y = [1,0,-1]

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))
    #for j in range(m):
    #    arr[i][j] = 5


def func(x, y, d):
    if x == n-1 and y == m-1:
        return arr[x][y]
    ret = dp[x][y][d]
    if ret != MIN:
        return ret


    for i in range(3):
        xx = x+dir_x[i]
        yy = y+dir_y[i]
        if xx > -1 and yy > -1 and xx < n and yy < m and dp[xx][yy][3] == MIN:
            dp[xx][yy][3] = 1
            dp[x][y][d] = ret = max(ret, func(xx, yy, i) + arr[x][y])
            dp[xx][yy][3] = MIN
    return ret


print(func(0,0,0))
