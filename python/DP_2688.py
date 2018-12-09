import sys

dp = [[(-1) for i in range(10)] for ii in range(65)]

for j in range(10):
    dp[0][j] = 1

def func(n):
    for i in range(1,n+1):
        ret = 0
        for j in range(10):
            dp[i][j] = dp[i-1][j] + ret
            ret += dp[i-1][j]
    return ret
for t in range(int(sys.stdin.readline())):
    print(func(int(sys.stdin.readline())))
