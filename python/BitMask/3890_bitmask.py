import sys
input = lambda:sys.stdin.readline().strip()

def func(cur, bit):
    if cur==11:
        return 0
    ret = 0
    for i in range(11):
        if arr[cur][i] and bit ^ 1<<i:
            ret = max(ret, func(cur+1, bit ^ 1<<i)+arr[cur][i])
    return ret

for c in range(int(input())):
    arr = [[] for i in range(11)]
    for i in range(11):
        arr[i] = list(map(int, input().split()))
    print(func(0,0))
