import sys
input = lambda:sys.stdin.readline().strip()

def DFS(cur,skip): #현재위치와 스킵가능한 값
    que = set()
    dfs = []
    que.add((cur,skip))
    ret = []
    while que:
        node, s = que.pop()
        print(node)
        dfs.append(arr[node])
        if len(dfs) == 6:
            ret.append(dfs)
            dfs = []
        for i in range(min(s, len(edge[node]))):
            que.add((node+1+i, s-i))
        #print(que)

    return ret
while 1:
    temp = list(map(int,input().split()))
    n = temp[0]
    arr = temp[1:]
    if n==0:
        break
    edge = []
    for i in range(n):
        edge.append(arr[i+1:])
    for i in range(n-6+1):
        print(DFS(i,n-6-i))
