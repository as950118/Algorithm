import sys
input = lambda:sys.stdin.readline().strip()
def func(x,y):
    if check[y][x]:
        return 0
    for _x in range(x+1, n):
        if check[y][x] or core[]
    for _y in range(y+1, n):

for t in range(int(input())):
    n = int(input())
    arr = []
    core = []
    check = [[0 for i in range(n)] for ii in range(n)]
    for y in range(n):
        temp = list(map(int, input().split()))
        core.append(list(i for i in range(n) if temp[i]))
        for x in core:
            check[y][x] = 2
        arr.append(temp)
    func(0,0)
