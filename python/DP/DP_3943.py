import sys

for t in range(int(sys.stdin.readline())):
    ret = val = int(sys.stdin.readline())
    while val != 1:
        if val%2==0:
            val //= 2
        else:
            val = (val*3) + 1
            ret = max(ret, val)
    print(ret)
