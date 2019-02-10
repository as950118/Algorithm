import sys
n,m=map(int, input().split())
arr = []
visited = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    arr.append(list(int(i) for i in sys.stdin.readline().strip()))
dirx = [0,0,1,-1]
diry = [-1,1,0,0]
def func():
    visited[0][0] = 1 #몇칸이나 지나왔는지
    bfs = []
    bfs.append((0,0))
    while bfs:
        x,y = bfs.pop(0) #bfs배열 가장 앞에 있는 원소를 꺼냄
        if x==m-1 and y==n-1:
            return visited[y][x]
        for i in range(4):
            newx = dirx[i] + x
            newy = diry[i] + y
            if newx>-1 and newx<m and newy>-1 and newy<n and not visited[newy][newx] and arr[newy][newx]:
                visited[newy][newx] = visited[y][x] + 1 #지나온 길이에 +1
                bfs.append((newx, newy)) #갈수있는 길이라면 bfs배열에 추가

print(func())
