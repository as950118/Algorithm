import sys
import math
#import os
#import time
#import multiprocessing
sys.setrecursionlimit(1000000000)
#from collections import deque


n, m = map(int, input().split())
arr_x = [[0]*(n) for i in range(m)]
dp_x = [[-1]*(n) for i in range(m)]
dp_x = [[-1]*(n) for i in range(m)]
dp_xy = [[-1]*(n) for i in range(m)]
direction = list(range(1,n))

for i in range(n):
    arr_x[i] = list(map(int, input().split()))

arr_y = arr_x
print(arr_y, arr_x)
def func_x(x,y):
    if dp_x[x][y] != -1:
        return dp_x[x][y]
    dp_x[x][y] = 1
    print(x,y)
    if x+1<n and arr_x[x+1][y] == 1:
        temp = 1
        temp = temp + func_x(x+1, y)
        dp_x[x][y] = max(dp_x[x][y], temp)
    return dp_x[x][y]
def func_y(x,y):
    if dp_y[x][y] != -1:
        return dp_y[x][y]
    dp_y[x][y] = 1
    if y+1<m and arr_y[x][y+1] == 1:
        temp = 1
        temp = temp + func_y(x+1, y)
        dp_y[x][y] = max(dp_y[x][y], temp)
    return dp_y[x][y]

for i in range(m):
    func_x(0,i)
for i in range(n):
    func_y(i,0)

for i in range(n):
    for j in range(m):
        if dp_x[i][j] == dp_x[i][j]:
            dp_xy[i][j] = dp_x[i][j]
print(max(dp_x))
