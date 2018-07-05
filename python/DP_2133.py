import sys
sys.setrecursionlimit(1000000000)
debug = 1
while debug:
    n = int(input())
    dp = [0]*10001
    '''
    2 = 3
    4 = 3*3 + 2*5 - 1 = 18
    6 = 222 or 24 3*3*3 + 3*18 = 3*27 = 81
    8 =
    '''
    for i in range(2, n+1, 2):
        dp[i] = (i-1)*(3**(i-1))
    print(dp[n])
    debug = 1
