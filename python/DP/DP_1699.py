import sys
import math
sys.setrecursionlimit(1000000000)
dp = [0]*10000001
ret=0
sqrt=0
min=0
'''
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
1 2 3 1 2 3 4 2 1 2  3  3  2  3  4  1  2  2  3  2  3  3
'''
debug = 1
while debug:
    n = int(input())
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n+1):
        dp[i*i] = 1
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        sqrt = int(math.sqrt(i))
        min = 10000
        for j in range(sqrt, 0, -1):
            temp = 1 + dp[i - j*j]
            if min>temp:
                min = temp
                dp[i] = min
    print(dp[n])
    debug=0
