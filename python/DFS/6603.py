import sys
input = lambda:sys.stdin.readline().strip()

def dfs(start, level):
    if level==6:
        for i in range(6):
            print(ret[i], end=" ")
        print("")
        return 0

    for i in range(start, n):
        ret[level] = arr[i]
        dfs(i+1, level+1)

while 1:
    temp = list(map(int,input().split()))
    ret = [0 for i in range(6)]
    arr = temp[1:]
    n = temp[0]
    if n==0:
        break
    dfs(0,0)
    print("")
