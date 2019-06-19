import sys
INF = sys.maxsize
input = lambda:sys.stdin.readline().strip()



'''
1234 100
456
'''
m = int(input())
remain = list(map(int, input().split()))
n = int(input())
make = list(map(int, input().split()))

remain.sort()
make.sort()
made = [0 for i in range(n)] #만든 파이프
def making(cur, val, goal):
    if cur==n:
        if val==0:
            return INF
        else:
            return val
    if made[cur] == 1:
        return making(cur+1, val)
    if goal==make[cur]:
        made[cur] = 1
        return val+1
    elif goal<make[cur]:
        return making(cur+1, val)
    else:
        return



for i in range(m):
    for j in range(n):
        ret += func(j,0,remain[i])
