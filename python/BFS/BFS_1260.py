import sys
#Deque를 사용할 필요 없음

n ,m ,v = map(int, sys.stdin.readline().strip().split())

edge = [[] for ii in range(n+1)]

for i in range(m):
	a, b = map(int, sys.stdin.readline().strip().split())
	edge[a].append(b)
	edge[b].append(a)

for e in edge: #내림차순으로 정렬
	e.sort(reverse=True)

def DFS():
	dfs = []
	stack = [v]
	visit = [0 for i in range(n+1)]
	while stack:
		node = stack.pop()
		if visit[node]:
			pass
		else:
			visit[node] = 1
			dfs.append(node)
			stack += edge[node]
	return dfs

def BFS():
	bfs = []
	que = [v]
	visit = [0 for i in range(n+1)]
	visit[v] = 1
	while que:
		node = que.pop()
		bfs.append(node)
		for i in reversed(edge[node]):
			if visit[i]:
				continue
			visit[i] = 1
			que = [i] + que
	return bfs

print(" ".join(map(str, DFS())))
print(" ".join(map(str, BFS())))
