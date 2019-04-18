import sys

def my_pop(n, cur):
    if cur >= 0:
        return stack[cur], cur-1
    else:
        return 0, cur


def hanoi(n, f, b, t):
    stack = []
    flag = 1
    cur = -1
    while flag:
        while n>1:
            stack.append(t)
            stack.append(b)
            stack.append(f)
            stack.append(n)
            n -= 1
            stack.append(t)
            t = b
            b,cur = my_pop(b,cur)

            if stack:
                if cur >= 0:
                    n = stack[cur]
                    cur -= 1
                else:
                    n = 0
                if cur >= 0:
                    n = stack[cur]
                    cur -= 1
                else:
                    n = 0
                if cur >= 0:
                    n = stack[cur]
                    cur -= 1
                else:
                    n = 0
