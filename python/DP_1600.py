import sys
arr =[0]
dp = [(-1) for i in range(1000)]
for i in range(10000):
    arr.append(arr[len(arr)-1]+i)
    if arr[len(arr)-1] > 300000:
        break
def func(n):
    for i in range(600):
        for j in range(arr[i], n+1):
            if i>1:
                dp[j] = min(dp[j-arr[i]]+1, dp[j])
            elif i==1:
                dp[j] = dp[j-arr[i]]+1
        if dp[i]>=n:
            break
    return dp[n]
print(func(int(sys.stdin.readline())))
