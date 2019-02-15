import sys
from collections import deque
arr = []
for i in range(int(sys.stdin.readline().strip())):
    arr.append(int(sys.stdin.readline().strip()))
arr.sort()
for i in arr:
    print(i)
