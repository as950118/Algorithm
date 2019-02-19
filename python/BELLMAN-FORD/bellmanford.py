import sys
inf = sys.maxsize

graph =[
[inf, 4, 3],
[inf, inf, -1],
[-2, inf, inf]
]
N = len(graph)

def bellmanford(graph, root):
    dist = [inf for i in range(N)]
    pre = [None for i in range(N)]
    dist[root] = 0

    #Relax edge
    for i in range(N-1):
        for n in range(N):
            for next_n in range(N):
                if dist[next_n] > dist[n] + graph[n][next_n]:
                    dist[next_n] = dist[n] + graph[n][next_n]
                    pre[next_n] = n

    #Check negative cycle
    for n in range(N):
        for next_n in range(N):
            if dist[next_n] > dist[n] + graph[n][next_n]:
                return -1 #Negative cycle, 무한대로 줄어듬
                break

    return dist, pre
print(bellmanford(graph,0))
