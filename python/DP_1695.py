import sys

n = int(input())

arr = list(map(int, input().split()))

dp = [[(-1) for i in range(n)] for ii in range(n)]


def func(start, end):
    ret = 0
    if start==end:
        return 1
    if arr[start] != arr[end]:
        ret += func(start+1, end)
    else:
        ret += func(start+1, end-1)
    return ret
print(func(0, n-1))
