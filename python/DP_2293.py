import sys

n, k = map(int, sys.stdin.readline().split())
a = [0] * 101
d = [0] * 10001

for i in range(0,n):
    a[i] = int(sys.stdin.readline())

for i in range(a[0], k+1, a[0]):
    d[i] = 1

for i in range(1,n):
    if a[i]<k+1:#error
        d[a[i]] += 1
        for j in range(a[i]+1,k+1):
            d[j] += d[j - a[i]]

print(d[k])
'''
import sys
sys.setrecursionlimit(1000000000)
debug=1
while debug:
    n, k = input().split()
    n = int(n)
    k = int(k)
    arr = [0]*101
    dp = [0]*10001
    for i in range(0, n):
        arr[i] = int(input())

    for i in range(arr[0], k+1, arr[0]):
        dp[i] = 1

    for i in range(1, n):
        dp[arr[i]] += 1
        for j in range(arr[i]+1, k+1):
            dp[j] = dp[j] + dp[j-arr[i]]

    print(dp[k])
    debug=0
'''
