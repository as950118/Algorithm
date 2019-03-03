import sys
input = lambda:sys.stdin.readline().strip()
import queue
INF = sys.maxsize
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split()))[1:])
len_groupA = n #그룹A의 크기
len_groupB = m #그룹B의 크기
matched = [0 for i in range(len_groupA)] #매칭되었는지를 체크
groupA = [-1 for i in range(len_groupA)] #0~3만 사용할 것이므로
groupB = [-1 for i in range(len_groupB+1)] #4~8만 사용할거지만, 편의상 크게해줌
dist = [INF for i in range(len_groupA)] #그룹A의 Node들의 Level

def bfs(): #그룹A의 Node들의 Level을 매기기 위해서
    Q = queue.Queue()
    for i in range(len_groupA):
        if not matched[i]: #매칭되어있지않으면 level은 0으로 시작
            dist[i] = 0
            Q.put(i)
        else:
            dist[i] = INF

    while not Q.empty(): #그룹A의 Node들의 Level을 측정
        a = Q.get(0)
        for b in graph[a]:
            if groupB[b] != -1 and dist[groupB[b]] == INF:
                dist[groupB[b]] = dist[a] + 1
                Q.put(groupB[b])

def dfs(a):
    for b in graph[a]: #그룹A의 a번째 Node와 연결되어있는 그룹B의 b중에서
        #(매칭되어있지않거나, b에 연결된 a'와 a의 Level이 1차이 나거나), (b에 연결되어있는 a'가 (매칭되어있지않거나, level이 1차이 나면))
        if groupB[b] == -1 or dist[groupB[b]] == dist[a] + 1 and dfs(groupB[b]):
            matched[a] = 1
            groupA[a] = b
            groupB[b] = a
            return 1
    return 0

match = 0 #매칭숫자
while 1:
    bfs()
    flow = 0
    for i in range(len_groupA):
        if not matched[i] and dfs(i):
            flow += 1
    if flow == 0: #더이상 매칭이없다면 종료
        break
    match += flow
print(match)
