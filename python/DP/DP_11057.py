import sys
sys.setrecursionlimit(1000000000)
'''
dp[1] = 10
dp[2] = 10+9+8+7+6+5+4+3+2+1
dp[3] = 10+9*2...
dp[4] =
0 1 2 3 4 5 6 7 8 9 dp[1] = 10
0 1 2 3 4 5 6 7 8 9 dp[2] = 55 = 10 9 8 7 6 5 4 3 2 1
0 1 2 3 4 5 6 7 8 9 dp[3] = 220 = dp[2]  dp[2]-dp[1] dp[2]-dp[1]-(dp[1]-1)55 + 45 + 36 + 28 + 21 + 15 + 10 + 6 + 3 + 1
0 1 2 3 4 5 6 7 8 9 dp[4] =      dp[3]  dp[3]-dp[2]  220 + 165 + 120 + 84 + 56 + 35 + 20 + 10 + 4+ 1
                    dp[5] = dp[4] + do[4]-dp[3] + (do[4]-dp[3])-dp[2] + ((do[4]-dp[3])-dp[2])-(dp[2]-i)
'''

dp = [[0]*11 for i in range(1001)]
ret=0
def func(n, i):
    if n<i:
        return 0
    dp[i][1] = dp[i-1][0]
    for j in range(2,11):
        dp[i][j] = dp[i][j-1]-dp[i-1][j-1]
    for j in range(1,11):
        dp[i][0] += dp[i][j]


    func(n, i+1)


n = int(input())
dp[1][0] = 10
for i in range(1, 11):
    dp[1][i] = 1
func(n, 2)
if dp[n][0] >= 10007:
    dp[n][0] = dp[n][0]%10007
print(dp[n][0])
