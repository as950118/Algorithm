import sys
def input(): # 편의를 위하여
	return sys.stdin.readline().strip()

n = int(input())
temp = list(map(int, input().split()))
temp[int(input())] = None
edge = [[] for i in range(n)]
for i in range(n):
	try:
		if temp[i] == -1:
			continue
		edge[temp[i]].append(i)
	except:
		pass
try:
	v = temp.index(-1)


	def BFS_right():#edge는 Node간의 관계 / v는 Root Node
		ret = 0
		bfs = []
		que = [v]
		visit = [0 for i in range(n+1)]
		visit[v] = 1
		while que:
			node = que.pop()
			bfs.append(node)
			temp = que[:]
			for i in reversed(edge[node]):
				if visit[i]:
					continue
				visit[i] = 1
				que = [i] + que
			if temp==que:
				ret += 1
		return ret

	print(BFS_right())
except:
	print(0)
