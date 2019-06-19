import sys
sys.setrecursionlimit(10**6)
INF = sys.maxsize

n,m = map(int, input().split())
def func(start,goal):
    if goal%start != 0:
        return INF
    ret = 0
    goal = goal//start
    while goal%3 == 0:
        goal //= 3
        ret += 1
    while goal%2 == 0:
        goal //= 2
        ret += 1
    return ret

ret = func(n,m)
if ret==INF:
    print(-1)
else:
    print(ret)
