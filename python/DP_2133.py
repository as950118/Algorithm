import sys
sys.setrecursionlimit(1000000000)
debug = 1
while debug:
    n = int(input())
    dp = [0]*10001
    '''
    2 = 3
    4 = 3*3 + 2 = 11
    6 = 3*3*3 + 3*2 + 2*3 = 3*(9+2+2) + 3*13 = 39
    8 = 3*3*3*3 + 3*2*3 + 2*3*3 + 3*3*2 + 2*2 = 9*(9+6+6+6) + 4 = 9*27 + 4 = 247
    10 =
    2 =
    22 4 =
    222 //24 42 =
    2222 /224 242 422/ 44 =
    22222 /2224 2242 2422 4222/ 244 424 442 =
    222222 /22224*5 2244*6/ 444 =
    3
    3**2+ 2
    3**3+ 32*2
    3**4+ 332*3+ 22
    3**5+ 3332*4+ 322*3
    3**6 33332*5 3322*6 222
    3**7 333332*6 33322*10 3222*4
    3**8 3333332*7 333322*15 33222*10 2222

    '''
    dp[2] = 3
    dp[4] = 11
    for i in range(6, n+1, 2):
        dp[i] = dp[i-2]*4 - dp[i-4]
    print(dp[n])
    debug = 0
