import sys
sys.setrecursionlimit(10**6)
dir_x = [-1,1,1,-1,-1,1,0,0]
dir_y = [-1,1,-1,1,0,0,-1,1]
def func(y,x):
    if arr[y][x] == 1:
        arr[y][x] = 0
        for i in range(8):
            cur_y = y+dir_y[i]
            cur_x = x+dir_x[i]
            if -1 < cur_y and cur_y < h and -1 < cur_x and cur_x < w:
                func(cur_y, cur_x)

while 1:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    arr = [[] for i in range(h)]
    for i in range(h):
        arr[i] = list((map(int, input().split())))
    ret=0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                func(i,j)
                ret += 1
    print(ret)
