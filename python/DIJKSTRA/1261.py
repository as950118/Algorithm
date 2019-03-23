import sys
import queue
INF = sys.maxsize

#미로에 관한 입력 받기
m,n = map(int, input().split())
maze = []
for i in range(n):
    maze.append(sys.stdin.readline().strip())

#이동방향
dirx = [0,0,-1,1]
diry = [-1,1,0,0]

dist = [[INF for i in range(m)] for ii in range(n)] #(0,0)에서 (x,y)까지 부순벽
dist[0][0] = 0 #0,0은 0이므로 0으로 설정
def dijkstra():
    q = queue.PriorityQueue() #우선순위 큐를 생성
    q.put((0,0,0)) #x,y,현재까지 부순벽
    dist[0][0] = 0 #부순벽
    while not q.empty():
        curx, cury, curd = q.get() #큐에서 꺼냄
        #이동방향에 따라서 진행
        for i in range(4):
            newx = curx + dirx[i]
            newy = cury + diry[i]
            newd = curd
            #미로를 벗어나지 않는 이동 가능한 방향이라면
            if -1<newx and newx<m and -1<newy and newy<n:
                #만약 벽이 있다면
                if maze[newy][newx] == '1':
                    #부순벽을 +1 해줌
                    newd = curd + 1
                #만약 현재(newx,newy)까지 부순벽보다
                #벽을 부수고 난 값(newd)이 더 적다면
                #queue에 넣음
                if dist[newy][newx] > newd:
                    dist[newy][newx] = newd
                    q.put((newx,newy,newd))
    return dist[n-1][m-1]

print(dijkstra())
