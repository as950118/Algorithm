import sys

n = int(input())
dp = [0 for i in range(n+1)]
dp[1] = 0
for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if i%2==0:
        temp = dp[i//2] + 1
        if dp[i] > temp:
            dp[i] = temp
        #dp[i] = min(dp[i-1], dp[i//2]) + 1
    if i%3 ==0:
        temp = dp[i//3] + 1
        if dp[i] > temp:
            dp[i] = temp
        #dp[i] = min(dp[i//3], dp[i-1], dp[i//2]) + 1
print(dp[n])
'''
1      ->      n
  2,3,4,5,6...
2 -> 1+1 1x2
3 -> 2+1 1x3
4 -> 2x2 3+1
5 -> 4+1
.
.
.
n -> n-1 +1 / n//2 * 2 / n//3 * 3
'''
