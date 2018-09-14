import sys
sys.setrecursionlimit(1000000000)

def func(cur, move, time):#cur, move, time
    temp = dp[time][move][cur]
    if temp != -1:
        return temp

    temp = 0
    if arr[time] == cur:
        temp = 1

    if time == t:
        return temp
    if move == w:
        temp += func(cur, move, time+1)
        return temp
    temp += max(func(cur, move, time+1), func(3-cur, move+1, time+1))

    return temp


t, w = map(int, sys.stdin.readline().split())
arr = [0]*(t+1)
for i in range(t):
    #arr[i+1] = int(input())
    if i%2==1:
        arr[i+1] = 1
    else:
        arr[i+1] = 2
dp = [[[-1]*(2+1) for i in range(w+1)] for j in range(t+1)]
print(func(1,0,0))
