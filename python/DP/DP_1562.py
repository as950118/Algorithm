import sys
sys.setrecursionlimit(10000000)

MOD = 1000000000

n = int(input())
dp = [[[(-1) for i in range(1<<10)] for ii in range(n)] for iii in range(10)]
ret = 0
def func(val, idx, dir):
    if val>9 or val<0:
        return 0
    dir = dir|(1<<val)
    if idx == n:
        if dir == (1<<10)-1:
            return 1
        return 0
    if dp[val][idx][dir] != -1:
        return dp[val][idx][dir]

    dp[val][idx][dir] = (func(val+1, idx+1, dir) + func(val-1, idx+1, dir))%MOD
    return dp[val][idx][dir]

for i in range(1,10):
    ret+=func(i,1,0)

print(ret)
