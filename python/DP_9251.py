import sys
sys.setrecursionlimit(1000000000)
from collections import deque


arr = list(input())
arr2 = list(input())
len_arr = len(arr)
len_arr2 = len(arr2)
ret=0

def func(a, b, sum):
    global ret
    if a==len_arr:
        return 0
    for i in range(a, len_arr):
        for j in range(b, len_arr2):
            if arr[i]==arr2[j]:
                func(i+1, j+1, sum+1)
                break
    ret = max(ret, sum)
func(0,0, 0)
print(ret)
