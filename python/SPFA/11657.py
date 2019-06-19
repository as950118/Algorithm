import sys
inf = sys.maxsize
input = lambda:sys.stdin.readline().strip()
import queue

N, M = map(int, input().split())
edge = [[] for i in range(N)]
for i in range(M):
    a,b,c = map(int, input().split())
    edge[a-1].append((b-1, c))


def spfa(edge, root):
    q = queue.Queue()
    dist = [inf for i in range(N)]
    inQ = [0 for i in range(N)] #queue 안에 들어있는값
    cycle = [0 for i in range(N)]

    dist[root] = 0
    q.put(root)
    cycle[root] += 1

    while not q.empty():
        node = q.get(0)
        #q.pop()
        inQ[node] = 0

        for next_n, next_d in edge[node]:
            if dist[next_n] > dist[node] + next_d:
                dist[next_n] = dist[node] + next_d

                if not inQ[next_n]:
                    cycle[next_n] += 1
                    
                    #Check negative cycle
                    if cycle[next_n] >= N:
                        return [-1] #무한대로 줄어듬
                    q.put(next_n)
                    inQ[next_n] = 1
    return dist[1:]

for i in spfa(edge, 0):
    if i==inf:
        print(-1)
    else:
        print(i)
