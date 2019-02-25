import sys
input = lambda : sys.stdin.readline().strip()
n = int(input())
m = int(input())
edge = [[sys.maxsize for i in range(n)] for i in range(n)]
for i in range(m):
    a,b,c=map(int, input().split())
    edge[a-1][b-1]= c
    edge[b-1][a-1]= c

def prim():
    key = [sys.maxsize for i in range(n)]
    parent = [None for i in range(n)]
    key[0] = 0
    mstset = [0 for i in range(n)]
    for i in range(n):
        min_d = sys.maxsize
        min_n = None
        for j in range(n):
            if key[j]<min_d and not mstset[j]:
                min_d = key[j]
                min_n = j
        mstset[min_n] = 1
        for k in range(n):
            if edge[min_n][k] and not mstset[k] and key[k] > edge[min_n][k]:
                key[k] = edge[min_n][k]
    return sum(key)
print(prim())
