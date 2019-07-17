import sys
from collections import deque
input = lambda:sys.stdin.readline().strip()
INF = sys.maxsize

def bfs(): #그룹A의 Node들의 Level을 매기기 위해서
    que = deque()
    for a in range(1,m+1):
        if len(groupA[a])<maximum: #매칭 개수가 2개가 안넘으면 level은 0으로 시작
            dist[a] = 0
            que.append(a)
        else:
            dist[a] = INF
    dist[0] = INF
    while que: #그룹A의 Node들의 Level을 측정
        a = que.popleft()
        if dist[a] < dist[0]:
            for b in graph[a]:
                if dist[groupB[b]] == INF:
                    dist[groupB[b]] = dist[a] + 1
                    que.append(groupB[b])
    return dist[0] != INF

def dfs(a):
    if a:
        for b in graph[a]: #그룹A의 a번째 Node와 연결되어있는 그룹B의 b중에서
            #(b에 연결된 a'와 a의 Level이 1차이 나거나), (b에 연결되어있는 a'가 (매칭되어있지않거나, level이 1차이 나면))
            if dist[groupB[b]] == dist[a] + 1 and dfs(groupB[b]):
                groupA[a].append(b)
                groupB[b] = a
                return 1
        dist[a] = INF
        return 0
    return 1


n,m = map(int, input().split())
graph = [[] for i in range(m+1)]
maximum = (n//2)

for i in range(1,n+1):
    graph[int(input())].append(i)
groupA = [[] for i in range(m+1)]
groupB = [0 for i in range(n+1)]
dist = [INF for i in range(m+1)] #그룹A의 Node들의 Level
match = 0 #매칭숫자
while bfs():
    for a in range(1, m+1):
        if len(groupA[a])<maximum: #매칭 개수가 2개가 안넘으면
            match += dfs(a)
        if len(groupA[a])<maximum: #매칭 개수가 2개가 안넘으면
            match += dfs(a)
print(groupA)
print(match)
