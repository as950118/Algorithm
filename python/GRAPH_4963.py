'''
설명은
https://blog.naver.com/na_qa/221458629301
'''
import sys
sys.setrecursionlimit(10**6) #재귀를 위해
dir_x = [-1,1,1,-1,-1,1,0,0] #8방향으로 이동하기위해
dir_y = [-1,1,-1,1,0,0,-1,1] #8방향으로 이동하기위해
def func(y,x):
    if arr[y][x] == 1:
        arr[y][x] = 0
        for i in range(8):
            cur_y = y+dir_y[i]
            cur_x = x+dir_x[i]
            if -1 < cur_y and cur_y < h and -1 < cur_x and cur_x < w: #범위를 벗어나지 않도록
                func(cur_y, cur_x)

while 1:
    w,h=map(int,input().split())
    if w==0 and h==0: #종료할 경우
        break

    arr = [[] for i in range(h)]
    for i in range(h):
        arr[i] = list((map(int, input().split())))
    ret=0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1: #지도상에 1지점(섬)일 경우
                func(i,j)
                ret += 1 #섬의 개수 +1
    print(ret)
