import sys
import math
#import os
#import time
#import multiprocessing
sys.setrecursionlimit(1000000000)
#from collections import deque


n = int(input())
arr = list(map(int, input().split()))
dp_a = [-1]*(n)
dp_b = [-1]*(n)
dp_c = [-1]*(n)

ret = 0
direction = list(range(1,n))

def func1(cur):
    global ret
    if dp_a[cur] != -1:
        return dp_a[cur]
    dp_a[cur] = 1
    for i in direction:
        if cur+i>-1 and cur+i<n and arr[cur] > arr[cur+i]:
            temp = 1
            temp = temp + func1(cur+i)
            dp_a[cur] = max(dp_a[cur], temp)

    return dp_a[cur]


def func2(cur):
    global ret
    if dp_b[cur] != -1:
        return dp_b[cur]
    dp_b[cur] = 1
    for i in direction:
        i = -1*i
        if cur+i>-1 and cur+i<n and arr[cur] > arr[cur+i]:
            temp = 1
            temp = temp + func2(cur+i)
            dp_b[cur] = max(dp_b[cur], temp)

    return dp_b[cur]

for i in range(n):
    func1(i)
    func2(i)

for i in range(n):
    dp_c[i] = dp_a[i] + dp_b[i]
ret = max(dp_c)

print(ret-1)
