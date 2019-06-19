import sys
inf = sys.maxsize

graph =[
[inf, 4, 3],
[inf, inf, -1],
[-2, inf, inf]
]
N = len(graph)

#Making edge
edge = [[] for i in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] != inf:
            edge[i].append((j, graph[i][j]))

def bellmanford(edge, root):
    dist = [inf for i in range(N)]
    pre = [None for i in range(N)]
    dist[root] = 0

    #Relax edge
    for i in range(N-1):
        for n in range(N):
            for next_n, next_d in edge[n]:
                if dist[n] != inf:
                    if dist[next_n] > dist[n] + next_d:
                        dist[next_n] = dist[n] + next_d
                        pre[next_n] = n

    #Check negative cycle
    for n in range(N):
        for next_n, next_d in edge[n]:
            if dist[n] != inf:
                if dist[next_n] > dist[n] + next_d:
                    return -1 #Negative cycle, 무한대로 줄어듬
                    break

    return dist, pre
print(bellmanford(edge,0))
