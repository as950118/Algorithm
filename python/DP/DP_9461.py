import sys
sys.setrecursionlimit(1000000000)

dp = [0]*100001

dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
def func(n, i):
    if n<i:
        return 0
    if dp[i] !=0:
        pass
    else:
        dp[i] = dp[i-2]+dp[i-3]
    func(n, i+1)
n=int(input())
for i in range(0, n):
     p = int(input())
     func(p, 4)
     print(dp[p])
