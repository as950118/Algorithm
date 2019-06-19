import sys
input = lambda:sys.stdin.readline().strip()

r,c = map(int, input().split())
arr = []
for i in range(r):
    arr.append(input())

dirx = [0,0,-1,1]
diry = [-1,1,0,0]
visitalp = set()
visitarr = [[0 for i in range(c)] for ii in range(r)]
def DFS(x,y):
    que = set()
    que.add((x,y,arr[y][x])) #x,y, 방문한 알파벳
    ret = 1
    while que:
        x,y,alp = que.pop()
        for i in range(4):
            newx = x+dirx[i]
            newy = y+diry[i]
            if -1<newx and newx<c and -1<newy and newy<r and not arr[newy][newx] in alp:
                que.add((newx, newy, alp + arr[newy][newx]))
                if ret < len(alp)+1: #깊이를 측정하기 위해
                    ret = len(alp)+1
    return ret

print(DFS(0,0))
