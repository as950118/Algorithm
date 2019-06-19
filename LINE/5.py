c ,b = map(int,input().split())

def BFS():
    bfs = []
    que = []
    que.append([c,b,1])
    while que:
        co, br, n = que.pop()
        if co == br:
            return n-1
        if br<1 or co>200000 or br>200000:
            continue
        que = [[co+n, br-1, n+1],[co+n, br+1, n+1],[co+n, br*2, n+1]] + que
    return -1
print(BFS())
