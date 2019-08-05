n=int(input())
choo = list(map(int, input().split()))
m=int(input())
goo = list(map(int, input().split()))

def func(val, idx, ret):
    if val==ret:
        return 1
    if val>ret:
        return 0
    if idx==n:
        return 0
    for next_idx in range(idx,n):
        if func(val+choo[next_idx],next_idx+1,ret) or func(val,next_idx+1,ret+choo[next_idx]):
            return 1
    return 0

for i in range(m):
    if func(0,0,goo[i]):
        print("Y", end=" ")
    else:
        print("N", end=" ")
