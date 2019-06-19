import sys
sys.setrecursionlimit(1000000000)

n, k = map(int, sys.stdin.readline().split())
arr = [0]*101
dp = [100001]*100001
dp[0] = 0
for i in range(1, n+1):
    arr[i] = int(input())

for i in range(1, n+1):
    for j in range(arr[i], k+1):
        dp[j] = min(dp[j], dp[j-arr[i]]+1)
if dp[k]==100001:
    dp[k] = -1
print(dp[k])
