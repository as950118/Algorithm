import sys
input = lambda:sys.stdin.readline().strip()
dirx = [0,0,-1,1]
diry = [-1,1,0,0]
def DFS(i,j):
    stack = [(i,j)]
    while stack:
        y,x = stack.pop()
        if not arr[y][x]: #이미 방문한 배추라면 패스함
            pass
        else:
            arr[y][x] = 0 #배추를 방문한후, 0으로 처리해줌
            for i in range(4):
                newy = y+diry[i]
                newx = x+dirx[i]
                if -1<newy and newy<n and -1<newx and newx<m and arr[newy][newx]:
                    stack.append((newy,newx)) #연결되어있는 배추를 stack에 삽입해줌
    return 1
for t in range(int(input())):
    ret = 0
    #배추에 관한 정보를 입력받음
    m,n,k = map(int, input().split())
    arr = [[0 for i in range(m)] for ii in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        arr[y][x] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1: #만약 집이있다면, dfs를 시작함
                ret += DFS(i,j)
    print(ret)
