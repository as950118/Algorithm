import sys
sys.setrecursionlimit(1000000000)
debug = 1
def func(n, i):
    global ret
    while 1:
        if i**2==n:
            ret+=1
            return 0
        if i**2 > n:
            i-=1
            n = n-i**2
            ret+=1
            func(n, 1)
            return 0
        else:
            i+=1
while debug:
    ret=0
    n = int(input())
    func(n, 1)
    print(ret)

    debug=1
