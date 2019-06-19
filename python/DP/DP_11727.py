'''
1 = 1 last 1 = 1 / 2 = 0
2 = 2 last 1 = 1 / 2 = 1
3 = 3 last 1 = 2 / 2 = 1
4 = 5 last 1 = 3 / 2 = 2
5 = 8      1 = 5 / 2 = 3
6 = 13     1 = 8 / 2 = 5
7 = 18     1 = 13 / 2 = 8
'''

dp = [0]*1001
dp[0] = 0
dp[1] = 1
dp[2] = 3
dp[3] = 5

def func(n, i):
    if n<i:
        return 0
    dp[i] = dp[i-1]+dp[i-2]*2
    if 10007<=dp[i]:
        dp[i] = dp[i] % 10007
    func(n, i+1)


n = int(input())
func(n, 4)
print(dp[n])
