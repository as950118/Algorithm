import sys
input = lambda:sys.stdin.readline().strip()

def DFS(s): #s는 시작노드
    stack = edge[s][:] #edge를 복사할때 [:]를 이용하여 얕은복사(값만복사)
    visit = [0 for i in range(n)]
    while stack:
        node = stack.pop()
        if visit[node]: #이미 방문한 노드라면 패스함
            pass
        else:
            visit[node] = 1 #방문 현황을 표시함
            ret_arr[s][node] = 1 #s와 node는 연결되어있다는 의미
            stack = stack + edge[node] #현재 Node의 Child를 가장 뒤쪽에 삽입함

#경로에 관한 정보를 입력
n = int(input())
edge = [[] for i in range(n)] #관계
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j]==1:
            edge[i].append(j)

ret_arr = [[0 for i in range(n)] for ii in range(n)] #결과값
for i in range(n):
    if edge[i]: #edge가 있다면
        DFS(i) #DFS 실행

#결과 출력
for i in range(n):
    for j in range(n):
        print(ret_arr[i][j], end=" ")
    print("")
