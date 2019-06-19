import sys
sys.setrecursionlimit(10001)

dp = [[0]*4 for i in range(10001)]
arr = [0]*10001

def func(n, i):
    if n<i:
        return 0
    dp[i][0] = max(max(dp[i-1][2], dp[i-1][1]), dp[i-1][0])
    dp[i][1] = dp[i-1][0] + arr[i]
    dp[i][2] = dp[i-1][1] + arr[i]
    func(n, i+1)
n = int(input())

for i in range(1, n+1):
    arr[i] = int(input())

dp[1][1] = arr[1]
dp[2][0] = arr[1]
dp[2][1] = arr[2]
dp[2][2] = arr[1] + arr[2]

func(n, 3)
print(max(max(dp[n][0], dp[n][1]), dp[n][2]))
