import sys

n,m = map(int, sys.stdin.readline().strip().split())
edge = [[] for i in range(n)]
for i in range(m):
    y,x = map(int, sys.stdin.readline().strip().split())
    edge[y-1].append(x-1)
    edge[x-1].append(y-1)

visit = [0 for i in range(n)]
ret = 0
for i in range(n):
    #dfs
    if not visit[i]:
        stack = set()
        stack.add(i)
        while stack:
            node = stack.pop() #오른쪽부터 탐색하는 경우의 DFS임
            visit[node] = 1 #방문 현황을 표시함
            for j in edge[node]:
                if not visit[j]:
                    stack.add(j) #현재 Node의 Child를 가장 뒤쪽에 삽입함
        ret += 1
print(ret)
