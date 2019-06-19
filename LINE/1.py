import sys
import math
N = int(input())

W = math.sqrt(N)
for w in range(int(W),N+1):
    if N%w==0:
        h = N//w
        if h>w:
            print(h-w)
            break
        else:
            print(w-h)
            break
