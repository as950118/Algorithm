import sys
sys.setrecursionlimit(1000000000)
from collections import deque
import mymodule

n = int(input())
m = int(input())
temp = [int(input()) for i in range(m)]
temp.insert(0,0)
arr = [-1]*(n+1)
dp = [-1]*(n+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

start = 3

def func(i):
    global start
    if dp[i] != -1:
        return dp[i]

    for j in range(start, i+1):
        dp[j] = dp[j-1] + dp[j-2]
    start = i

    return dp[i]

ret = 1

ret_temp = 0

for i in range(1, n+1):
    try:
        if temp.index(i):
            ret *= func(ret_temp)
            ret_temp = 0
    except:
        if i==n:
            ret *= func(ret_temp+1)
        else:
            ret_temp += 1

print(ret)
