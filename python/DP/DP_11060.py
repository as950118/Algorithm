import sys
sys.setrecursionlimit(1000000000)
from collections import deque

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [-1]*(n)
ret = -1

def func(a,b):
    global ret
    if a==n-1:
        if ret == -1:
            ret = b
        else:
            ret = min(ret, b)
        return 1
    l = arr[a]
    temp = 0
    temp_i = 0
    for i in range(1, l+1):
        if a+i<n:
            if a+i==n-1:
                func(a+i, b+1)
                return 0
            if i + arr[a+i]>temp_i + temp:
                temp = arr[a+i]
                temp_i = i
    if temp_i != 0:
        func(a+temp_i, b+1)
    return 0

func(0,0)
print(ret)
