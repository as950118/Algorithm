N,e,w,s,n = map(int, input().split())
percent = [e/100,w/100,s/100,n/100]
Map = [[0 for i in range(N*2+1)] for ii in range(N*2+1)]
dirX = [1,-1,0,0]
dirY = [0,0,-1,1]
def func(count, x,y):
    if count==N:
        return 1
    Map[x][y] = 1
    ret = 0
    for i in range(4):
        X = x+dirX[i]
        Y = y+dirY[i]
        if Map[X][Y]:
            continue
        ret += func(count+1,X,Y)*percent[i]
    Map[x][y] = 0
    return ret

print(func(0,N,N))
