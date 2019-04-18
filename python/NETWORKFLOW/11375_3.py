import sys
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = sys.maxsize

def bfs(us, pair_u, pair_v, dist, adj):
    queue = deque()
    for u in range(m+1,n+m+1):
        if pair_u[u] == -1:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = INF
    dist[-1] = INF
    while queue:
        u = queue.popleft()
        if dist[u] < dist[-1]:
            for v in adj[u]:
                if dist[pair_v[v]] == INF:
                    dist[pair_v[v]] = dist[u] + 1
                    queue.append(pair_v[v])
    return dist[-1] != INF


def dfs(u, adj, dist, pair_v, pair_u):
    if u != -1:
        for v in adj[u]:
            if dist[pair_v[v]] == dist[u]+1:
                if dfs(pair_v[v], adj, dist, pair_v, pair_u):
                    pair_v[v] = u
                    pair_u[u] = v
                    return True
        dist[u] = INF
        return False
    return True


def hopcroft_karp(us, adj):
    dist = defaultdict(lambda: -1)
    pair_u = defaultdict(lambda: -1)
    pair_v = defaultdict(lambda: -1)
    matching = 0
    while bfs(us, pair_u, pair_v, dist, adj):
        for u in us:
            if pair_u[u] == -1:
                if dfs(u, adj, dist, pair_v, pair_u):
                    matching += 1
    return matching



n, m = map(int, sys.stdin.readline().strip().split())
ns = [i+m+1 for i in range(n)]
adj = [None for i in range(n+m+1)]

for i in range(n):
    adj[i+1+m] = list(map(int, sys.stdin.readline().strip().split()))[1:]

print(hopcroft_karp(ns, adj))
