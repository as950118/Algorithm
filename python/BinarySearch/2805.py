import sys
input = lambda:sys.stdin.readline().strip()

n,m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort(reverse=True)
tree.append(0)

arr = []
temp = 0
for i in range(n):
    for j in range(tree[i]-tree[i+1]):
        temp+=i+1
        arr.append(temp)

def binarysearch():
    lo = 0
    hi = len(arr)-1
    while 1:
        if lo>hi:
            return lo
        mid = (lo+hi)//2
        val = arr[mid]
        if val == m:
            return mid
        elif val>m:
            hi = mid-1
        else:
            lo = mid+1

print(len(arr)-1-binarysearch())
