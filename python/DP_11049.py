import sys
sys.setrecursionlimit(1000000000)
from collections import deque

n = int(sys.stdin.readline())
arr = [[-1]*(2) for i in range(n+1)]
for i in range(n):
    arr[i+1] = int(input().split())

def func(cur, val):
