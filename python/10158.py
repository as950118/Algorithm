import sys
input = lambda:sys.stdin.readline().strip()

w,h = map(int, input().split())
p,q = map(int, input().split())
t = int(input())
def func(start, size):
    mod = t%(2*size)
    size_start = size-start
    size_2_start = size*2 - start
    size_2_start_mod = size*2 - start - mod

    if mod == 0:
        ret = start
    elif mod == size_start:
        ret = size
    elif mod < size_start:
        ret = start + mod
    elif mod > size_start:
        if mod == size_2_start:
            ret = 0
        elif mod == (size_start)*2:
            ret = start
        elif mod < size_2_start:
            ret = size_2_start_mod
        else:
            ret = -size_2_start_mod
    return ret
print(func(p,w), func(q,h))
