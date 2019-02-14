import sys
def input():
    return sys.stdin.readline().strip()
n = int(input())
m = int(input())
edge = [[] for i in range(n)]
sel = [0 for i in range(n)]
for i in range(m):
    a,b,c=map(int, input().split())
    edge[a-1].append((b-1,c))
    edge[b-1].append((a-1,c))

mst = []
sel[0] = 0
for i in range(len(edge[0])):
    x,y = edge[0][i].pop(0)
    mst.append((-y, x))
ret = 0
start = 0
end = 0
while mst:
    start, end = mst.pop(0)
