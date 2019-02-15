import sys
MAX = 300001
dp = [(0) for i in range(MAX)]
arr = []
n = int(input())
for i in range(0, MAX):
    temp = int(i*(i+1)*(i+2)/6)
    if temp>n:
        break
    arr.append(temp)
for i in range(1, n+1):
    dp[i] = MAX
    for j in arr:
        if j > i:
            if j == i:
                dp[i] = 0
            break
        if dp[i]>dp[i-j]:
            dp[i] = dp[i-j]
    dp[i] += 1
print(dp[n])
