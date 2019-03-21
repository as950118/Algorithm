import sys
input = lambda:sys.stdin.readline().strip()

n = int(input().strip())
arr = list(map(int, input().strip().split()))
Max = sys.maxsize
ret = 0
for i in range(n):
    cur = arr[n-1-i]
    if Max==1:
        break
    if cur < Max:
        ret += cur
        Max = cur
    else: #cur>=Max
        ret += (Max-1)
        Max = (Max-1)
print(ret)


'''
def func(cur, val):
    if cur==0:
        return val
    else:
        if arr[cur-1] >= val:
            if val == 1:
                return val
            else:
                return val + func(cur-1, val-1)
        else:
            return val + func(cur-1, arr[cur-1])
print(func(n-1, arr[n-1]))
'''
'''
ret = 0
for i in range(1,n-1):
    temp = func(len(arr)-i, arr[len(arr)-i])
    if ret<temp:
        ret = temp

print(ret)
'''
