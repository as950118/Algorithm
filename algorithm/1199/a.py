import sys
inf = sys.maxsize
n,x,y = map(int, input().split())
arr = [inf for i in range(x)]+list(map(int, input().split()))+[inf for i in range(y)]

flag = 1
for i in range(x,n+x):
    flag=1
    for j in range(1,x+1):
        if arr[i]>arr[i-j]:
            flag=0
            break
    if flag:
        for k in range(1,y+1):
            if arr[i]>arr[i+k]:
                flag=0
                break
    if flag:
        print(i-x+1)
        break
