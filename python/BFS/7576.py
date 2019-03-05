import sys
from collections import deque
input = lambda:sys.stdin.readline().strip()

m,n = map(int, input().split())
box = []
que = deque()
for i in range(n):
    box.append(list(map(int, input().split())))
    for j in range(m):
        if box[i][j] == 1:
            que.append((i,j))
dirx = [0,0,-1,1]
diry = [-1,1,0,0]
def bfs():
    while que:
        y,x = que.popleft()
        for i in range(4):
            newy = y+diry[i]
            newx = x+dirx[i]
            if -1<newy and newy<n and -1<newx and newx<m and not box[newy][newx]:
                box[newy][newx] = box[y][x] + 1
                que.append((newy,newx))
def func():
    ret = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return 0
            ret = max(ret, box[i][j])
    return ret
bfs()
print(func() - 1)
