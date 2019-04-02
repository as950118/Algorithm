import sys
input = lambda:sys.stdin.readline().strip()
INF = sys.maxsize

#n, edge 입력
n = int(input())
edge = []
for i in range(n):
    edge.append(list(map(int, input().split())))

#Yes Bitmask 및 시작점 표시
yes = (1<<n) - 1
start = 0
temp = input()
for i in range(n):
    if temp[i]=='N':
        yes ^= 1<<i
    else:
        start += 1

#p 입력
p = int(input())

#DP
dp = [-1 for i in range((1<<n))]
def func(cur, bit):
    if cur >= p:
        return 0
    if dp[bit] != -1:
        return dp[bit]
    dp[bit] = INF
    for j in range(n):
        if bit & 1<<j:
            continue
        for i in range(j):
            if bit & 1<<i:
                dp[bit] = min(dp[bit], func(cur+1, bit^(1<<j))+edge[i][j])
        for i in range(j+1, n):
            if bit & 1<<i:
                dp[bit] = min(dp[bit], func(cur+1, bit^(1<<j))+edge[i][j])
    return dp[bit]

if start==0:
    if p==0:
        print(0)
    else:
        print(-1)
else:
    print(func(start,yes))
