import sys
import math
sys.setrecursionlimit(1000000000)
from collections import deque


t = int(input())
while t:
    arr = deque([0]*101)
    arr[0] = 1
    ret = 0
    n = int(input())
    for i in range(2, n+1):
        for j in range(i, n+1, i):
            if arr[j] == 0:
                arr[j] = 1
            elif arr[j] == 1:
                arr[j] =0
    for i in range(1, n+1):
        if arr[i] == 0:
            ret = ret+1
    print(ret)
    t = t-1
