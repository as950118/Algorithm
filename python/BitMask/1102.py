import sys
INF = sys.maxsize

n = int(input())
arr = []
edge = [[] for i in range(n)]
yes = [0 for i in range(n)]
visit = [0 for i in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(0,i):
        edge[i].append((j,arr[i][j]))
    for j in range(i+1,n):
        edge[i].append((j,arr[i][j]))
temp = input()
for i in range(n):
    if temp[i]=='Y':
        yes[i] = 1
    else:
        continue
p = int(input())
ret = INF
def func(cur, val, node):
    if cur == p:
        global ret
        ret = min(ret, val)
        return 0
    for next_n, next_d in edge[node]:
        if not visit[next_n]:
            visit[next_n] = 1
            func(cur+1, val+next_d, next_n)
            visit[next_n] = 0

for y in yes:
    visit[y] = 1
    func(1,0,y)
print(ret)
