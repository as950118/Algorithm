import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
pipe = defaultdict(lambda:defaultdict(list))
visit = defaultdict(lambda:0)
n = int(input())
for i in range(n):
    a,b,c = map(str, input().split())
    pipe[a][b] = int(c)
    pipe[b][a] = int(c)


def bfs(node, val):
    if visit[node]:
        print("Visit")
        return 0
    if node=="Z":
        print("Get Z")
        return val
    if not pipe[node]:
        print("Not pipe[node]")
        return -1
    ret = val
    visit[node] = 1
    for next_node in pipe[node]:
        print(next_node)
        if not pipe[node][next_node]:
            continue
        next_val = min(val, pipe[node][next_node])
        temp = bfs(next_node, next_val)
        if not temp:
            continue
        if temp==-1:
            del(pipe[node][next_node])
        ret = max(ret, temp)
    visit[node] = 0
    return ret

print(bfs("A",0))