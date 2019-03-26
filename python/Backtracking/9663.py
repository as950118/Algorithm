'''
col, row, left cross, right cross를 체크해줘야함
'''


n = int(input())
check = [0 for i in range(n)]
ret = 0
def checking(cur):
    print(check, cur)
    a - b = c - d
    b - a = c - d
    b = a-c+d
    b = a+c-d
    try:
        check[:cur].index(check[cur])
        check[:cur].index(check)
        return 0
    except:
        return 1
    for i in range(cur):
        if check[cur] == check[i]:
            return 0
        #if abs(cur-check[cur]) == abs(i-check[k]):
        if abs(check[cur] - check[i]) == (cur-i):
            return 0
    return 1

def backtracking(cur):
    if cur==n:
        global ret
        ret += 1
    else:
        for i in range(n):
            check[cur] = i
            if checking(cur):
                backtracking(cur+1)


backtracking(0)
print(ret)
