'''
설명은
https://blog.naver.com/na_qa/221458955810
'''
import sys
MAX = 10**9 #최대값
n = int(sys.stdin.readline().strip())
arr = [[MAX for i in range(n)] for ii in range(n)]
for i in range(n): #같은 지점으로 가는 방법은 없으므로
    arr[i][i] = 0
m = int(sys.stdin.readline().strip())

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split()) #readline과 input의 시간차이가 상당함
    if arr[a-1][b-1]>c: #-1을 해준 이유는, 1부터가 아니라 0부터 시작하기때문, 편의에 따라 설정
        arr[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            temp = arr[i][k] + arr[k][j] #정점사이의 여러가지 방벙
            if arr[i][j]>temp:
                arr[i][j]=temp

for i in range(n):
    for j in range(n):
        if arr[i][j]!=MAX: #만약 가는 방법이 없다면 예외처리를 해줘야함
            print(arr[i][j], end=" ")
        else:
            print(0, end=" ")
    print("")
