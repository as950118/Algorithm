import sys
input = lambda:sys.stdin.readline().strip()

dirx = [0,0,-1,1]
diry = [-1,1,0,0]

def DFS(x,y):
    stack = set()
    stack.add((x,y))
    Ret = 0
    while stack:
        x,y = stack.pop() #오른쪽부터 탐색하는 경우의 DFS임
        if not arr[y][x]:
            pass
        arr[y][x] = 0 #방문 현황을 표시함
        Ret += 1
        for i in range(4):
            newx = x+dirx[i]
            newy = y+diry[i]
            if -1<newx and newx<n and -1<newy and newy<m and arr[newy][newx]:
                stack.add((newx,newy))
    return Ret


m,n,k = map(int, input().split())
arr = [[1 for i in range(n)] for ii in range(m)]
for i in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[j][i] = 0
ret = 0
area = []
for i in range(n):
    for j in range(m):
        if arr[j][i]:
            area.append(DFS(i,j))
            ret += 1
print(ret)
area.sort()
for elem in area:
    print(elem, end=" ")
