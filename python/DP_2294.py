import sys
sys.setrecursionlimit(1000000000)

n, k = input().split()
n = int(n)
k = int(k)
arr = [0]*101
dp = [0]*10001
for i in range(0, n):
    arr[i] = int(input())
def func(n, i, k):
    if n<i:
        return k
    for j in range(1, n):
        dp[i] = dp[i-1] + arr[j]
        if dp[i] == 15:
            return k
        elif dp[i]>15:
            dp[i] = -1
            return -1
        else:
            func(n, i, k+1)

print(func(n,1,0))
