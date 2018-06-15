import sys
sys.setrecursionlimit(1000000)


dp = [0]*1000000
arr = [0]*1000000
ret = 0

def func(n, i):
    if n<i:
        return 0
    if dp[i-1]+arr[i-1]<0:
        dp[i] = 0
    else:
        dp[i] = arr[i-1] + dp[i-1]

    if dp[i]<dp[i-1]:
        if func2(n, i+1)==-1:
            dp[n] = dp[i-1]
            return 0

    func(n, i+1)

def func2(n, i):
    if n<i:
        return -1
    if arr[i-1]<0:
        return func2(n, i+1)
    else:
        return 1

def func3(n, i):
    global ret
    if n<i:
        return ret

    else:
        ret = max(arr[i-1], ret)
        func3(n, i+1)

n = int(input())

arr = input().split()

for i in range(0, n):
    arr[i] = int(arr[i])

dp[1] = arr[0]
func(n, 2)
if dp[n]==0:
    ret= arr[0]
    func3(n,1)
    print(ret)
else:
    print(dp[n])
