import sys
inf = sys.maxsize
input = lambda:sys.stdin.readline().strip()

N, M = map(int, input().split())
edge = [[] for i in range(N)]
for i in range(M):
    a,b,c = map(int, input().split())
    edge[a-1].append((b-1, c))

def bellmanford(edge, root):
    dist = [inf for i in range(N)]
    #pre = [None for i in range(N)]
    dist[root] = 0

    #Relax edge
    for i in range(N-1):
        for n in range(N):
            for next_n, next_d in edge[n]:
                if dist[n] != inf: #예외처리 중요
                    if dist[next_n] > dist[n] + next_d:
                        dist[next_n] = dist[n] + next_d
                        #pre[next_n] = n

    #Check negative cycle
    for n in range(N):
        for next_n, next_d in edge[n]:
            if dist[n] != inf: #예외처리 중요
                if dist[next_n] > dist[n] + next_d:
                    return [-1] #Negative cycle, 무한대로 줄어듬
                    break

    return dist[1:]
for i in bellmanford(edge, 0):
    if i==inf:
        print(-1)
    else:
        print(i)
