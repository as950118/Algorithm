import sys
inf = sys.maxsize
input = lambda:sys.stdin.readline().strip()

N, M = map(int, input().split())
graph = [[inf for i in range(N)] for i in range(N)]
for i in range(M):
    a,b,c = map(int, input().split())
    graph[a-1][b-1] = c

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

    return dist
temp = bellmanford(graph,0)  
