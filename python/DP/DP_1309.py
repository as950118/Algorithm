import sys
sys.setrecursionlimit(1000000000)
from collections import deque
'''
1 3 7 17 41
'''
n = int(input())
arr = deque([1, 3])
tmp = 0

#arr2 = deque([[0]*(n) for i in range(n)])
for i in range(1, n):
    tmp = arr[1]
    arr[1] = arr[0] + arr[1]*2
    arr[0] = tmp
print(arr[1]%9901)
