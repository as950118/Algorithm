import sys
import queue
INF = sys.maxsize

n, e = map(int, sys.stdin.readline().strip().split())
edge = [[] for i in range(n)]
for i in range(e):
    a,b,c = map(int, sys.stdin.readline().strip().split())
    edge[a-1].append((b-1, c))
    edge[b-1].append((a-1, c))

def dijkstra(start, end):
    dist = [INF for i in range(n)]

    q = queue.PriorityQueue() #우선순위 큐를 생성
    q.put((start, 0)) #현재까지의 거리, 현재노드
    dist[start] = 0 #시작점에서 도착지점사이의 거리

    while not q.empty():
        cur_n, cur_d = q.get()

        if dist[cur_n] < cur_d: #만약 시작노드에서 현재노드까지 직접 연결하는 거리가 지금까지 거쳐온 거리보다 짧다면, 더이상 진행하지 않고 직접 연결하는 거리를 최소값으로 하고 해당노드에 대해서는 더 이상 탐색하지 않음
            continue
        for next_n in edge[cur_n]: #현재 노드에 연결된 노드들에 관해서
            next_d = cur_d + next_n[1] #현재까지의 거리와 다음 노드까지의 거리의 합이
            if dist[next_n[0]] > next_d: #직접 연결하는 경우보다 짧을경우
                dist[next_n[0]] = next_d #최소거리를 갱신하고
                q.put((next_n[0], next_d)) #최소거리에 대한 값을 큐에 넣어줌
    ret = []
    for i in end:
        ret.append(dist[i])
    return ret

#지나야 하는 두개의 정점
p1, p2 = map(int, input().split())

zero_to_p1, zero_to_p2 = dijkstra(0, [p1-1, p2-1])
p1_to_p2 = dijkstra(p1-1, [p2-1])[0]
p1_to_n, p2_to_n = dijkstra(n-1, [p1-1, p2-1])
ret = min(zero_to_p1 + p2_to_n, zero_to_p2 + p1_to_n) + p1_to_p2

#셋중에 하나라도 만약 경로가 없다면 -1을 출력
if ret>=INF:
    print(-1)
#모두 경로가 있다면 총합을 출력
else:
    print(ret)
