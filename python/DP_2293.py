import sys
sys.setrecursionlimit(1000000000)

n, k = input().split()
n = int(n)
k = int(k)
arr = [0]*101
dp = [0]*10001
for i in range(0, n):
    arr[i] = int(input())

for i in range(0, k+1, arr[0]):
    if i:
        dp[i] = 1

for i in range(1, n):
    dp[arr[i]] += 1
    for j in range(arr[i]+1, k+1):
        dp[j] = dp[j] + dp[j-arr[i]]

print(dp[k])
