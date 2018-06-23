import sys
sys.setrecursionlimit(1000000000)

dp = [0]*1000000
arr = [0]*1000000
arr2 = [0]*1000000
ret = 0

def func(n, i):
    global ret
    dp[i] = 1;
    if n<i:
        return 0
    for j in range(1, i):
        if arr2[i]>arr2[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    ret = max(ret, dp[i])
    func(n, i+1)



N = int(input())

arr = input().split()

for i in range(0, N):
    arr2[i+1] = int(arr[i])

func(N, 1)
print(ret)
