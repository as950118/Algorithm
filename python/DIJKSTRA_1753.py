import sys
INF = sys.maxsize
V, E = map(int, input().split())

K = int(input())
arr = [[INF for i in range(V)] for ii in range(V)]

for i in range(E):
    u,v,w=map(int, sys.stdin.readline().strip().split())
    arr[u-1][v-1] = w

def dijkstra():
    visited = [0 for i in range(V)]
    d = [INF for i in range(V)]
    d[K-1] = 0
    while 1:
        m = INF
        n = -1
        for i in range(V):
            if not visited[i] and m>d[i]:
                m = d[i]
                n = i
        if m == INF:
            break

        visited[n] = 1

        for i in range(V):
            if visited[i]:
                continue
            via = d[n] + arr[n][i]
            if d[i] > via:
                d[i] = via
    return d

d = dijkstra()
for i in d:
    print(i if i !=INF else "INF")
