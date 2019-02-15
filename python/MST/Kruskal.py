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
edge = []
for y in range(len(graph)):
    for x in range(len(graph[y])):
        if graph[y][x] != inf:
            edge.append((graph[y][x], x, y)) #편하게 sort하기 위해 가중치를 맨 앞으로
N = len(graph) #Node의 개수
def kruskal():
    edge.sort() #Edge 가중치대로 정렬
    parent = [] #순환인지 확인하기위해
    rank = []
    ret = []
    num_edge = 0
    num_node = 0

    for n in range(N):
        parent.append(n)
        rank.append(0)
    while num_edge < N-1: #연결된 Edge의 개수가 Node개수 -1 만큼 되면 종료
        e, x,y = edge[num_node]
        num_node += 1
        while parent[x] != x:
            x = parent[x]
        while parent[y] != y:
            y = parent[y]
        if x==y:
            continue
        num_edge += 1
        ret.append([x,y])
        if rank[x]<rank[y]:
            parent[x]=y
        elif rank[x]>rank[y]:
            parent[y]=x
        else:
            parent[y]=x
            rank[x]+=1
    return ret
print(kruskal())
