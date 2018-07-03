import sys
sys.setrecursionlimit(1000000000)

n, m = input().split()
n = int(n)
m = int(m)
arr = [[0]*m for i in range(n)]
arr2 = [[0]*m for i in range(n)]
dp = [0]*1000001
for i in range(0, n):
    arr[i] = input().split()
    for j in range(0, m):
        arr[i][j] = int(arr[i][j])
def func(n,i, x,y , _x,_y):
    if x==_x and y==_y:
        return 0
    elif x==_x:
        dp[i] = max(dp[i], dp[i-1] + arr[x][y+1])
        func(n+m-1, i+1, x, y+1, _x,_y)
    elif y==_y:
        dp[i] = max(dp[i], dp[i-1] + arr[x+1][y])
        func(n+m-1, i+1, x+1, y, _x,_y)
    else:
        dp[i] = max(dp[i], dp[i-1] + arr[x][y+1])
        func(n+m-1, i+1, x, y+1, _x,_y)
        dp[i] = max(dp[i], dp[i-1] + arr[x+1][y])
        func(n+m-1, i+1, x+1, y, _x,_y)

dp[0] = arr[0][0]
func(n+m, 1, 0,0, n-1,m-1)
print(dp[n+m-2])
