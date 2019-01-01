import sys
def input(): # 편의를 위하여
	return sys.stdin.readline().strip()

n = int(input())
temp = list(map(int, input().split()))
temp[int(input())] = None
edge = [[] for i in range(n)]
for i in range(n):
	try:
		edge[i].append(temp[i])
		edge[temp[i]].append(i)
	except:
		pass
print(edge)
v = temp.index(-1)


def BFS_right():#edge는 Node간의 관계 / v는 Root Node
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

print(BFS_right())
