from collections import deque #직관적으로 표현하기위해서 양방향으로 입출력이 가능한 deque를 사용함

def DFS_left(edge, v):#edge는 Node간의 관계 / v는 Root Node
	dfs = deque()
	stack = deque([v])
	visit = [0 for i in range(n+1)]
	while stack:
		node = stack.popleft() #왼쪽부터 탐색하는 경우의 DFS임
		if visit[node]: #이미 방문한 노드라면 패스함
			pass
		else:
			visit[node] = 1 #방문 현황을 표시함
			dfs.append(node) #DFS에 추가함
			stack = deque(edge[node]) + stack #현재 Node의 Child를 가장 앞쪽에 삽입함
	return dfs

def DFS_right(edge, v):#edge는 Node간의 관계 / v는 Root Node
	dfs = []
	stack = set()
	stack.add(v)
	visit = [0 for i in range(n+1)]
	while stack:
		node = stack.pop() #오른쪽부터 탐색하는 경우의 DFS임
		if visit[node]: #이미 방문한 노드라면 패스함
			pass
		else:
			visit[node] = 1 #방문 현황을 표시함
			dfs.add(node) #DFS에 추가함
			for child in edge[node]:
				stack.add(child) #현재 Node의 Child를 가장 뒤쪽에 삽입함
	return dfs
