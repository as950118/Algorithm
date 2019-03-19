import sys
import queue
sys.setrecursionlimit(100000)
INF = sys.maxsize

m,n = map(int, input().split())
maze = []
for i in range(n):
    maze.append(sys.stdin.readline().strip())
dirx = [0,0,-1,1]
diry = [-1,1,0,0]
dist = [[INF for i in range(m)] for ii in range(n)]
dist[0][0] = 0
def dijkstra():
    q = queue.PriorityQueue() #우선순위 큐를 생성
    q.put((0,0,0)) #x,y,현재값
    dist[0][0] = 0 #부순벽
    while not q.empty():
        curx, cury, curd = q.get()
        if dist[cury][curx] > curd:
            continue
        for i in range(4):
            newx = curx + dirx[i]
            newy = cury + diry[i]
            newd = curd
            if -1<newx and newx<m and -1<newy and newy<n:
                if maze[newy][newx] == '1':
                    newd += 1
                if dist[newy][newx] > newd:
                    dist[newy][newx] = newd
                    q.put((newx,newy,newd))

dijkstra()
print(dist[n-1][m-1])
