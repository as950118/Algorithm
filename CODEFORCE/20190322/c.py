import sys
input = lambda:sys.stdin.readline().strip()

n,k=map(int,input().split())
edge = [[] for i in range(n)]
for i in range(n-1):
    u,v,w = map(int, input().split())
    edge[u-1].append((v-1,w))
    edge[v-1].append((u-1,w))
ret = [INF for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if edge[i][k] + edge[k][j]
