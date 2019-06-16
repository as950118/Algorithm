import sys
from collections import defaultdict, deque
INF = sys.maxsize
sys.setrecursionlimit(10**6)
graph = defaultdict(lambda:defaultdict(int))

#A to Z
def bfs(start, sink, parent):
    visited = defaultdict(lambda:0)
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        u = queue.popleft()
        for ind in graph[u]:
            val = graph[u][ind]
            if visited[ind]:
                continue
            if val <= 0:
                continue
            queue.append(ind)
            visited[ind] = 1
            parent[ind] = u
    return 1 if visited[sink] else 0

def ford_fulkerson(start, sink):
    parent = defaultdict(lambda:-1)
    max_flow = 0
    while bfs(start, sink, parent):
        path_flow = INF
        s = sink
        while s!=start:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v!=start:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

print(ford_fulkerson("A","Z"))