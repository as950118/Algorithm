import sys
input = lambda:sys.stdin.readline().strip()

m,n = map(int, input().split())
box = []
que = []
nop = []
for i in range(n):
    box.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            que.append((i,j))
        if box[i][j] == -1:
            nop.append((i,j))
dirx = [1,-1,0,0]
diry = [0,0,1,-1]

def func():
    bfs = []
    visit = [[0 for i in range(m)] for i in range(n)]
    for y,x in que:
        visit[y][x] = 1
    for y,x in nop:
        visit[y][x] = 1
    ret = -1
    while que:
        y,x = que.pop()
        bfs.append((y,x))
        temp = 0
        for i in range(4):
            newy = y+diry[i]
            newx = x+dirx[i]
            if -1<newy and newy<n and -1<newx and newx<m:
                if visit[newy][newx]:
                    continue
                visit[newy][newx] = 1
                que.append((newy,newx))
                temp += 1
        if temp == 0:
            continue
        else:
            ret += temp-1
    return ret
print(func())
