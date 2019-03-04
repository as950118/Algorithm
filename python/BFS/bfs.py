from collections import deque #양쪽으로 입출력이 가능한 Deque

def BFS_left():#edge는 Node간의 관계 / v는 Root Node
	bfs = deque()
	que = deque([v])
	visit = [0 for i in range(n+1)]
	visit[v] = 1
	while que:
		node = que.popleft()
		bfs.append(node)
		for i in edge[node]:
			if visit[i]:
				continue
			visit[i] = 1
			que.append(i)
	return bfs

def BFS_right(edge, v):#edge는 Node간의 관계 / v는 Root Node
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
