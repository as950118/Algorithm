import sys

def my_pop(n, cur, stack):
    if cur >= 0:
        return stack[cur], cur-1, stack[:cur]
    else:
        return 0, cur, stack


def hanoi(n, f, b, t):
    stack = []
    flag = 1
    cur = -1
    while flag:
        while n>1:
            print("adad")
            stack.append(t)
            stack.append(b)
            stack.append(f)
            stack.append(n)
            n -= 1
            stack.append(t)
            t = b
            b,cur,stack = my_pop(b,cur,stack)

            if stack:
                n,cur,stack = my_pop(n,cur,stack)
                f,cur,stack = my_pop(f,cur,stack)
                b,cur,stack = my_pop(b,cur,stack)
                t,cur,stack = my_pop(t,cur,stack)
                n -= 1
                stack.append(f)
                f = b
                b,cur,stack = my_pop(b,cur,stack)
            else:
                flag = 0
def Hanoi(n,f,b,t):
    if n==1:
        return 0
    else:
        Hanoi(n-1,f,b,t)
        Hanoi(n-1,b,f,t)

n = int(input())
print(hanoi(n,0,1,2))
