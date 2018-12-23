import sys
from collections import deque

n = int(sys.stdin.readline().strip())#정점 개수
temp = [[] for i in range(n+1)]
edge = [[] for i in range(n+1)]
dp = [[(0) for i in range(n+1)] for ii in range(2)]#얼리어답터일 경우와 아닐경우를 나눠서

for i in range(n-1):
	a,b = map(int, sys.stdin.readline().strip().split())
	temp[a].append(b)
	temp[b].append(a)

#BFS
bfs = deque()
Deque = deque([1])
visit = [(False) for i in range(n+1)]
visit[1] = True
while Deque:
	leftval = Deque.popleft()
	bfs.appendleft(leftval)
	for i in temp[leftval]:
		if visit[i]:
			continue
		visit[i] = True
		edge[leftval].append(i)
		Deque.append(i)


for i in bfs:
	dp[1][i] = 1
	for j in edge[i]:
		dp[0][i] += dp[1][j]
		dp[1][i] += min(dp[0][j], dp[1][j])
print(min(dp[0][1], dp[1][1]))
 ​
