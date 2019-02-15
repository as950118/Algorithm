import sys
sys.setrecursionlimit(1000000000)

n=int(input());
def maxScore(y,x):
    if(x>=m):return 0;
    if(d[y][x]!=-1):return d[y][x];
    if y==0:
        d[y][x]=max(maxScore(1,x+1),maxScore(1,x+2))+arr[y][x];
        return d[y][x];
    if y==1:
        d[y][x]=max(maxScore(0,x+1),maxScore(0,x+2))+arr[y][x];
        return d[y][x];
for i in range(n):
    m=int(input());
    arr=[0,0]
    arr[0]=list(map(int,input().split(' ')));
    arr[1]=list(map(int,input().split(' ')));
    d=[[-1]*m,[-1]*m];
    up=maxScore(0,0)
    d=[[-1]*m,[-1]*m];
    down=maxScore(1,0)
    print(max(up,down))
