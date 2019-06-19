import sys
input = lambda:sys.stdin.readline().strip()
dirx = [0,0,-1,1]
diry = [-1,1,0,0]
def DFS(i,j):
    stack = [(i,j)]
    ret = 0
    while stack:
        y,x = stack.pop()
        if not arr[y][x]: #이미 방문한 노드라면 패스함
            pass
        else:
            arr[y][x] = 0 #집을 방문한후, 0으로 처리해줌
            for i in range(4):
                newy = y+diry[i]
                newx = x+dirx[i]
                if -1<newy and newy<n and -1<newx and newx<n and arr[newy][newx]:
                    stack.append((newy,newx)) #연결되어있는 집을 stack에 삽입해줌
            ret += 1 #각 단지내 집의수를 +1 해줌
    return ret

rets = [] #각 단지내 집의수를 저장할 배열

#집에 관한 정보를 입력받음
n = int(input())
arr = [[]for i in range(n)]
for i in range(n):
    for j in input():
        arr[i].append(int(j))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: #만약 집이있다면, dfs를 시작함
            rets.append(DFS(i,j))

rets.sort() #각 단지내 집의수를 정렬
print(len(rets)) #총 단지수 출력
for i in rets: #각 단지내 집의수 출력
    print(i)
