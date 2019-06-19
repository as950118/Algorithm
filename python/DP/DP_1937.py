import sys
import math
#import os
#import time
#import multiprocessing
sys.setrecursionlimit(1000000000)
#from collections import deque


n = int(input())
arr = [[0]*(n) for i in range(n)]
dp = [[-1]*(n) for i in range(n)]
for i in range(n):
    arr[i] = list(map(int,input().split()))

ret = 1
direction_x = [-1, 1, 0, 0]
direction_y = [0 ,0, -1, 1]
#탐색 순서도 메모리 사용에 큰 영향을 끼침
def func(x, y):
    global ret

    if dp[x][y] !=-1:
        return dp[x][y]

    dp[x][y] = 1
    for k in range(4):
        i = direction_x[k]
        j = direction_y[k]
        if x+i>-1 and y+j>-1 and x+i<n and y+j<n and (arr[x+i][y+j] > arr[x][y]):
            temp = 1
            temp = temp + func(x+i, y+j)
            dp[x][y] = max(dp[x][y], temp)
            ret = max(dp[x][y], ret)

    return dp[x][y]

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            func(i,j)
print(ret)
