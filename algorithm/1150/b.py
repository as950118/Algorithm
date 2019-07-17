# -*- coding: utf-8 -*-
n=int(input())
arr = []
for i in range(n):
    temp = str(input())
    temp2 = []
    for i in temp:
        if i=='#':
            temp2.append(1)
        else:
            temp2.append(0)
    arr.append(temp2)


d_x = [0,0,-1,1]
d_y = [-1,1,0,0]

check = arr[:]

def func(x,y):
    if check[y][x]:
        return 0
    for i in range(4):
        if check[y+d_y[i]][x+d_x[i]]:
            return 0
    for i in range(4):
        check[y+d_y[i]][x+d_x[i]] = 1
    for ny in range(y,n):
        for nx in range(x,n):
            if func(nx,ny):
                return 1
    for i in range(4):
        check[y + d_y[i]][x + d_x[i]] = 1

    return 0
if func(1,1):
    print("YES")
else:
    print("NO")