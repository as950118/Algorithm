import sys
sys.setrecursionlimit(1000000000)
from collections import deque
import mymodule

n = int(input())
m = int(input())
temp = [int(input()) for i in range(m)]
arr = [-1]*(n)
dp = [-1]*(n)
for i in range(m):
    arr[temp[i]] = 0
