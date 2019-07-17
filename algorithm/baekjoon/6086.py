import sys
from collections import defaultdict, deque
INF = sys.maxsize
sys.setrecursionlimit(10**6)
pipe = defaultdict(lambda:defaultdict(int))
n = int(input())
for i in range(n):
    a,b,c = map(str, input().split())
    pipe[a][b] += int(c)
    pipe[b][a] += int(c)

#A to Z
def bfs(start, sink, parent):
    visited = defaultdict(lambda:0)
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        u = queue.popleft()
        for ind in pipe[u]:
            val = pipe[u][ind]
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
            path_flow = min(path_flow, pipe[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v!=start:
            u = parent[v]
            pipe[u][v] -= path_flow
            pipe[v][u] += path_flow
            v = parent[v]
    return max_flow

print(ford_fulkerson("A","Z"))