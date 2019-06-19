'''
col, row, cross를 체크해줘야함
'''

n = int(input())
check = [0 for i in range(n)]

def checking(cur):
    for i in range(cur):
        if check[cur] == check[i]: #row(y) 검사
            return 0
        if abs(check[cur] - check[i]) == (cur-i): #cross 검사
            return 0
    return 1

def backtracking(cur):
    if cur==n:
        return 1
    else:
        ret = 0
        for i in range(n): #col(x)을 기준으로 진행
            check[cur] = i
            if checking(cur): #둘수있는지 검사
                ret += backtracking(cur+1)
    return ret

print(backtracking(0))
