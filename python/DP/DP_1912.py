import sys
sys.setrecursionlimit(1000001)


dp = [0]*1000001
arr = [0]*1000001
ret = 0
debug = 1
while debug:
    n = int(input())

    arr = input().split()

    for i in range(0, n):
        arr[i] = int(arr[i])

    dp[0] = arr[0]
    ret = arr[0]

    for i in range(1, n):
        dp[i] = max(dp[i-1]+arr[i], arr[i])
        if(ret<dp[i]):
            ret = dp[i]

    print(ret)
    debug = 0
