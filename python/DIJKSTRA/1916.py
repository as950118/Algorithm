import sys
import queue
INF = sys.maxsize

V = int(input())
E = int(input())

edge = [[] for i in range(V)] #사작점에 대해서만 선언
dist = [INF for i in range(V)] #모든 거리에 대해 최대값으로 설정

for i in range(E):
    u,v,w=map(int, sys.stdin.readline().strip().split()) #input()보다 훨씬 빠름
    edge[u-1].append((v-1, w))

def dijkstra():
    q = queue.PriorityQueue() #우선순위 큐를 생성
    q.put((0, K-1)) #현재까지의 거리, 현재노드
    dist[K-1] = 0 #시작점에서 도착지점사이의 거리

    while not q.empty():
        pp = q.get()
        cur_n = pp[1] #현재 노드 위치
        cur_d = pp[0] #현재 거리

        if dist[cur_n] < cur_d: #만약 시작노드에서 현재노드까지 직접 연결하는 거리가 지금까지 거쳐온 거리보다 짧다면, 더이상 진행하지 않고 직접 연결하는 거리를 최소값으로 하고 해당노드에 대해서는 더 이상 탐색하지 않음
            continue
        for next_n in edge[cur_n]: #현재 노드에 연결된 노드들에 관해서
            next_d = cur_d + next_n[1] #현재까지의 거리와 다음 노드까지의 거리의 합이
            if dist[next_n[0]] > next_d: #직접 연결하는 경우보다 짧을경우
                dist[next_n[0]] = next_d #최소거리를 갱신하고
                q.put((next_d, next_n[0])) #최소거리에 대한 값을 큐에 넣어줌


K,y = map(int, input().split())
dijkstra()

print(dist[y-1])
