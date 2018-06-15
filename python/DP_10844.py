'''
1 = / 2 3 4 5 6 7 8 9
2 = 1 / 3 4 5 6 7 8 9
3 = 1 2 / 4 5 6 7 8 9
4 = 1 2 3 / 5 6 7 8 9
5 = 1 2 3 4 / 6 7 8 9
6 = 1 2 3 4 5 / 6 7 9
.
.
.
'''

import sys
sys.setrecursionlimit(1000000)

dp = [0]*1000000
ret = 0

def func(n, i, j, k):#횟수 위치 계단수 현재값
    global ret
    if n<=i:
        ret+=1
        return 0
    if k-j<0:
        if k+j<10:
            func(n, i+1, j, k+j)
        else:
            return 0
    elif k+j>9:
        if k-j>-1:
            func(n, i+1, j, k-j)
        else:
            print('sx')
            return 0
    else:
        func(n, i+1, j, k+j)
        func(n, i+1, j, k-j)



N = int(input())
for j in range(1, 9):
    for k in range(1, 10):
        func(N, 1, j, k)
print(ret)
