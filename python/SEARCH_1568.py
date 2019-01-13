n = int(input())
ret = 1

def func():
    global ret
    global n
    for i in range(1, 10**9):
        if n-i==0:
            return ret
        if n-i<0:
            return func()
        ret += 1
        n = n-i

print(func())
