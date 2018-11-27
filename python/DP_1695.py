import sys
import array

import time

n = int(sys.stdin.readline())
n = 5000
#arr = array.array('i', [-1] + list(map(int, sys.stdin.readline().split())))
#arr = [-1] + list(map(int, sys.stdin.readline().split()))
arr = [-1] + [i for i in range(n)]
start = time.time()
print(time.time()-start)
start = time.time()
dp = [[(0) for i in range(n+1)] for ii in range(2)]
print(time.time()-start)
start = time.time()

#print(n,arr,dp)
for i in range(n, 0, -1):
    for j in range(i, n+1):
        if arr[i] == arr[n-j+1]:
            dp[(i)%2][j] = dp[(i-1)%2][j-1] + 1
        else:
            dp[(i)%2][j] = max(dp[(i-1)%2][j], dp[(i)%2][j-1])
print(time.time()-start)

print(n - dp[(n)%2][(n)])
