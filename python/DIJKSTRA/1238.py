import sys
import queue
INF = sys.maxsize
input = lambda:sys.stdin.readline().strip()

n,m,x = map(int, input().split())

arr = [[INF for i in range(n)] for ii in range(n)]
for i in range(n): #같은 지점으로 가는 방법은 없으므로
    arr[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split()) #readline과 input의 시간차이가 상당함
    if arr[a-1][b-1]>c: #-1을 해준 이유는, 1부터가 아니라 0부터 시작하기때문, 편의에 따라 설정
        arr[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            temp = arr[i][k] + arr[k][j] #정점사이의 여러가지 방벙
            if arr[i][j]>temp:
                arr[i][j]=temp

ret = [0 for i in range(n)]
for i in range(n):
    if i != x-1:
        if arr[i][x-1]!=INF: #만약 가는 방법이 없다면 예외처리를 해줘야함
            ret[i] += arr[i][x-1] + arr[x-1][i]
        else:
            pass
print(max(ret))
