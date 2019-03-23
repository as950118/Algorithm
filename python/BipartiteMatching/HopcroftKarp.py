import sys
import queue
input = lambda:sys.stdin.readline().strip()
INF = sys.maxsize


len_groupA, len_groupB, edge_n = map(int, input().split())
edge = [[] for i in range(len_groupA)]
for i in range(edge_n):
    u,v = map(int, input().split()) #Wegiht==1
    edge[u].append(v)

matched = [0 for i in range(len_groupA)] #매칭 여부
groupA = [-1 for i in range(len_groupA)] #어떤 b와 매칭되었는지
groupB = [-1 for i in range(len_groupB + len_groupB)] #어떤 a와 매칭되었는지, len_groupA+1 ~ len_groupA+len_groupB 까지 사용함
dist = [INF for i in range(len_groupA + len_groupB)] #Node들의 Level

def bfs(): #GroupA Node들의 Level을 매기기 위해
    Q = queue.Queue()
    for i in range(len_groupA): #매칭되어있는것들이 있는지 탐색
        if not matched[i]:
            dist[i] = 0
            Q.put(i)
        else:
            dist[i] = INF

    while not Q.empty():
        a = Q.get(0)
        for b in edge[a]: #b에 연결되어있는 b들 중에
            if groupB[b] != -1 and dist[groupB[b]] == INF: #b가 매칭이 안되어있고
                dist[groupB[b]] = dist[a] + 1
                Q.put(groupB[b])

def dfs(a):
    for b in edge[a]: #a에 연결되어있는 b들 중에
        #매칭되지 않았거나 / 매칭되었는데 b의 Level이 a보다 1 클 경우
        if groupB[b] == -1 or ( dist[groupB[b]] == dist[a]+1 and dfs(groupB[b]) ): #B에 연결된 값
                matched[a] = 1
                groupA[a] = b
                groupB[b] = a
                return 1
    return 0

match = 0 #매칭숫자

while 1:
    flow = 0
    bfs()
    for a in range(len_groupA):
        if not matched[a]:
            if dfs(a):
                flow += 1
    if flow == 0:
        break
    match += flow

print(match)
