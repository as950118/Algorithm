import sys
import queue
INF = sys.maxsize

graph = [[5],[4,6],[5,7],[6,7]]
len_groupB = 4
len_groupA = 4
matched = [0 for i in range(len_groupA)]
groupA = [-1 for i in range(len_groupA)]
groupB = [-1 for i in range(len_groupB + 4)]
dist = [INF for i in range(len_groupA)]
def bfs():
    Q = queue.Queue()
    for elem in matched:
        if not elem:
            dist[elem] = 0
            Q.put(elem)
        else:
            dist[i] = INF

    while not Q.empty():
        a = Q.get(0)
        Q.get()
        for b in graph[a]:
            if groupB[b] != -1 and dist[groupB[b]] == INF:
                dist[groupB[b]] = dist[a] + 1
                Q.put(groupB[b])
def dfs(a):
    for b in graph[a]:
        if groupB[b] != -1 or dist[groupB[b]] == dist[a] + 1 and dfs(groupB[b]):
            matched[a] = 1
            groupA[a] = b
            groupB[b] = a
            return 1
    return 0

match = 0
while 1:
    bfs()
    flow = 0
    for i in range(len_groupA):
        if not matched[i] and dfs(i):
            flow += 1
    if flow == 0:
        break
    match += flow
print(match)
