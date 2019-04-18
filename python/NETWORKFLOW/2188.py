import sys
input = lambda:sys.stdin.readline().strip()

n,m = map(int, input().split())
edge = [[]]
room = [0 for i in range(m+1)]
check = [0 for i in range(m+1)]

for i in range(n):
    edge.append(list(map(int, input().split()))[1:])
ret = 0

def func(v):
    if visit[v]:
        return 0
    visit[v] = 1
    for elem in edge[v]:
        if not room[elem]:
            room[elem] = v
            return 1
        if func(room[elem]):
            room[elem] = v
            return 1
    return 0

for i in range(1,n+1):
    visit = [None for i in range(n+1)]
    ret += func(i)
print(ret)
