import sys
input = lambda:sys.stdin.readline().strip()
inf = sys.maxsize
graph =[
[inf, 5, 4, inf, inf, inf],
[5, inf, 2, 7, inf, inf],
[4, 2, inf, 6, 11, inf],
[inf, 7, 6, inf, 3, 8],
[inf, inf, 11, 3, inf, 8],
[inf, inf, inf, 8, 8, inf]
]

N = len(graph) #Node의 개수

def prim():
    key = [inf for i in range(N)] #Key값
    parent = [None for i in range(N)] #부모노드, 연결상태인지를 표시하기위해
    key[0] = 0 #root node
    visited = [0 for i in range(N)] #방문 표시
    for i in range(N): #0번째 Node부터 탐색
        #현재 Node의 최소값을 찾기
        min_d = inf #연결된 Node의 Edge중 최소값
        min_n = None #최소값을 가지는 Node
        for j in range(N):
            if key[j]<min_d and not visited[j]:
                min_d = key[j]
                min_n = j
        visited[min_n] = 1 #찾았다면 방문
        #최소값을 가지는 Node에서 방문하지 않은 Node들을 방문하고, key값의 갱신여부를 탐색
        for k in range(N):
            if graph[min_n][k] and not visited[k] and key[k] > graph[min_n][k]:
                key[k] = graph[min_n][k]
                parent[k] = min_n
    return parent

print(prim())
