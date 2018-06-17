import sys
sys.setrecursionlimit(1000000000)

dp = [0]*1000000
arr = [0]*1000000
ret = 0
mod = 1000000000

def func(n, i):
    if n==i:
        return 0
    for j in range(0, n):
        dp[i] = dp[i-1] + arr[j]
        dp[i] =
    func(n, i+1)


N = int(input())

arr = input().split()

for i in range(0, N):
    arr[i] = int(arr[i])

func(N, 1)
print(dp[N])
