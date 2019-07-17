def func(cur, cval, val):
    if cur==len_core:
        global ret, ret_cval
        if ret_cval<=cval:
            if ret>val:
                ret = val
        return 0
    y,x = core[cur]
    if x==0 or x==n-1 or y==0 or x==n-1:
        func(cur+1, cval+1, val)
        return 0
    if check[y][:x] == [0 for i in range(x)]:
        check[y][:x] = [1 for i in range(x)]
        func(cur+1, cval+1, val+x)
        check[y][:x] = [0 for i in range(x)]
    if check[y][x+1:] == [0 for i in range(n-1-x)]:
        check[y][x+1:] = [1 for i in range(n-1-x)]
        func(cur+1, cval+1, val+(n-1-x))
        check[y][x+1:] = [0 for i in range(n-1-x)]

    for i in range(y):
        if check[i][x]:
            break
        if i==y-1:
            for j in range(y):
                check[j][x] = 1
            func(cur+1, cval+1, val+y)
            for j in range(y):
                check[j][x] = 0

    for i in range(y+1,n):
        if check[i][x]:
            break
        if i==n-1:
            for j in range(y+1,n):
                check[j][x] = 1
            func(cur+1, cval+1, val+(n-1-y))
            for j in range(y+1,n):
                check[j][x] = 0

for t in range(1,int(input())+1):
    ret = 10**10
    ret_cval = 0
    n = int(input())
    arr = []
    core = []
    check = [[0 for i in range(n)] for ii in range(n)]
    for y in range(n):
        arr.append(list(map(int, input().split())))
        temp = list((y,x) for x in range(n) if arr[y][x])
        core += temp
        for y,x in temp:
            check[y][x] = 1
    len_core = len(core)
    func(0,0,0)
    print('#%s'%t,ret)
