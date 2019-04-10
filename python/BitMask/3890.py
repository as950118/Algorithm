import sys
input = lambda:sys.stdin.readline().strip()

def func(cur):
    if cur==11:
        return 0
    ret = 0
    for i in range(11):
        if arr[cur][i] and not check[i]:
            check[i] = 1
            ret = max(ret, func(cur+1)+arr[cur][i])
            check[i] = 0
    return ret


for c in range(int(input())):
    check = [0 for i in range(11)]
    arr = [[] for i in range(11)]
    for i in range(11):
        arr[i] = list(map(int, input().split()))
    print(func(0))
