import sys
input = lambda:sys.stdin.readline().strip()
dp = [1,1,5,11]
dp_len = len(dp)
for t in range(int(input())):
    n = int(input())
    for i in range(dp_len,n+1):
        dp.append(dp[i-1] + 5*dp[i-2] + dp[i-3] - dp[i-4])
    print(dp[n], dp)
    dp_len = max(dp_len, n+1)
